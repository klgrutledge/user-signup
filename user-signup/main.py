#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi
import re


#validating user input
user_name = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return user_name.match(username)

#don't need to validate this user input for LC101 assignment, but included per Udacity
#def valid_password(password):
    #password = re.compile(r"^.{3,20}$")
    #return password.match(password)

#validating user input
e_mail = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
def valid_email(email):
    return e_mail.match(email)

#page_header = """
#<!DOCTYPE html>
#<html>
#<head>
    #<title>Signup</title>
#</head>
#<body>
    #<h1>
        #<a href="/">Signup</a>
    #</h1>
#"""

#page_footer = """
#</body>
#</html>
#"""

table_form = """
<!DOCTYPE html>
<html>
<head>
    <title>Signup</title>
</head>
<body>
    <h1>
        <a href="/">Signup</a>
    </h1>

<form action='/signup-verification' method="post">
<tbody>
    <tr>
        <td>
            <label for = "username">Username</label>
        </td>
        <td>
            <input type="text" name="username" value="%(username)s" required/><div style="color: red">%(username_error_message)s</div>
        </td>
    </tr>
    <br>

    <tr>
        <td>
            <label for = "password">Password</label>
        </td>
        <td>
            <input type="password" name="password" required/><div></div>
            <span class="error"></span>
        </td>
    </tr>
    <br>

    <tr>
        <td>
            <label for = "verify_password">Verify Password</label>
        </td>
        <td>
            <input type="password" name="verify_password" required/><div style="color: red">%(password_error_message)s</div>
            <span class="error"></span>
        </td>
    </tr>
    <br>

    <tr>
        <td>
            <label for = "email">Email (optional)</label>
        </td>
        <td>
            <input type="text" name="email" value="%(email)s" required/><div style="color: red">%(email_error_message)s</div>
            <span class="error"></span>
        </td>
    </tr>
    <br>

    <input type = "submit"/>
</form>
</body>
</html>
"""

class Index(webapp2.RequestHandler):

    def generate_form(self, username_error_message="", password_error_message="", email_error_message="", username="", password="", verify_password="", email=""):
        self.response.write(table_form % {"username_error_message": username_error_message,
                                    "password_error_message": password_error_message,
                                    "email_error_message": email_error_message,
                                    "username": username,
                                    "password": password,
                                    "verify_password": verify_password,
                                    "email": email})

    def get(self):
        self.generate_form()


        #error = self.request.get("error")

        #username = self.request.get("username")
        #password = self.request.get("password")
        #verify_password = self.request.get("verify_password")
        #email = self.request.get("email")

        #if error:
            #error_esc = cgi.escape(error, quote=True)
            #error_element = '<p class="error">' + error_esc + '</p>'
        #elif username:
            #error_esc = cgi.escape(username, quote=True)
            #error_element = '<p class="error">' + error_esc + '</p>'
        #elif password:
            #error_esc = cgi.escape(password, quote=True)
            #error_element = '<p class="error">' + error_esc + '</p>'
        #elif email:
            #error_esc = cgi.escape(username, quote=True)
            #error_element = '<p class="error">' + error_esc + '</p>'
        #else:
            #error_element = ''



class Signup_Verification(webapp2.RequestHandler):
    def generate_form(self, username_error_message="", password_error_message="", email_error_message="", username="", password="", verify_password="", email=""):
        self.response.write(table_form % {"username_error_message": username_error_message,
                                    "password_error_message": password_error_message,
                                    "email_error_message": email_error_message,
                                    "username": username,
                                    "password": password,
                                    "verify_password": verify_password,
                                    "email": email})

    def post(self):


        user_username = self.request.get('username')
        user_password = self.request.get('password')
        user_verify_password = self.request.get('verify_password')
        user_email = self.request.get('email')


        username = valid_username(user_username)
        email = valid_email(user_email)

        username_error_message = "Please enter a valid username."
        password_error_message = "Please ensure your passwords match."
        email_error_message = "Please enter a valid email."

        if (not username) and (user_password != user_verify_password) and (not email):
            self.generate_form(username_error_message = username_error_message, password_error_message = password_error_message, email_error_message = email_error_message,
                               username=user_username, password=user_password, email=user_email)

        elif (not username) and (user_password != user_verify_password):
            self.generate_form(username_error_message = username_error_message, password_error_message=password_error_message,
                                username=user_username)

        elif (user_password != user_verify_password) and (not email):
            self.generate_form(password_error_message = password_error_message, email_error_message = email_error_message,
                                email=user_email)

        elif (not username) and (not email):
            self.generate_form(username_error_message = username_error_message, email_error_message = email_error_message,
                                username=user_username, email=user_email)

        elif not username:
            self.generate_form(username_error_message = username_error_message, username=user_username)

        elif (user_password != user_verify_password):
            self.generate_form(password_error_message = password_error_message)

        elif not email:
            self.generate_form(email_error_message = email_error_message, email=user_email)

        else:
            self.response.write("Welcome, " + user_username + "!")

    #def post(self):
        #entered_username = self.request.get("username")
        #entered_password = self.request.get("password")
        #entered_password2 = self.request.get("verify_password")
        #entered_email = self.request.get("email")

        #validating username input - blank username
        #if entered_username == "":
            #error = "Please enter a username!"
            #self.redirect("/?error=Please enter a username!")

        #validating username input - username contains prohibited characters
        #validated_username = valid_username(entered_username)
        #if not validated_username:
            #error = "Please enter a valid username!"
            #self.redirect("/?error=Please enter a valid username!")

        #validating password and verify_password user inputs - entered passwords do not match
        #if entered_password != entered_password2:
            #error = "Your passwords do not match!"
            #self.redirect("/?error=Your passwords do not match!")

        #validating email input - email contains prohibited characters
        #validated_email = valid_email(entered_email)
        #if not validated_email:
            #error = "Please enter a valid email!"
            #self.redirect("/?error=Please enter a valid email!")

        #else:
            #self.redirect("/?welcome")


        #content = page_header + "<p>" + "Welcome, " + entered_username + "!" + "</p>" + page_footer
        #self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', Index),
    ('/signup-verification', Signup_Verification)],
    debug=True)
