from flask import Flask, request, redirect, render_template
import cgi
import re

app = Flask(__name__)
app.config['DEBUG'] = True

page_header = """
<!DOCTYPE html>
<html>
    <head>
        <title>User Sign-up</title>
    </head>
    <body>
"""

page_footer = """
    </body>
</html>
"""

@app.route("/add", methods=['POST'])
def add_user():
    new_user = request.form['newUser']
    new_Pass = request.form['newPass']
    new_vPass = request.form['verifyPass']
    new_email = request.form['newEmail']

    userName_error = ''
    pword_error = ''
    vPass_error = ''
    email_error = ''


    if (new_user.strip() == "") or (len(new_user) < 3 or len(new_user) > 20):
        userName_error = "Not a valid username"

    if (new_Pass.strip() == ""):
        pword_error = "Not a valid password"

    if (new_vPass.strip() == "") or (new_vPass != new_Pass):
        vPass_error = "Passwords don't match"

    if (new_email != ''):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", new_email):
            email_error = "Email not valid"

    if (userName_error != '') or (pword_error != ''):
        return render_template('signUp.html', email_error = email_error, vPass_error = vPass_error, pword_error = pword_error, userName_error = userName_error)

    sentence = "User has been added!"
    content = page_header + "<h1>" + sentence + "</h1>" + page_footer

    return content

@app.route("/")
def index():
    error = request.args.get("error")

    return render_template('signUp.html',
        error = error and cgi.escape(error, quote=True)
    )

app.run()
