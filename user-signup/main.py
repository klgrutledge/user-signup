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

page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Signup</title>
</head>
<body>
    <h1>
        <a href="/">Signup</a>
    </h1>
"""

page_footer = """
</body>
</html>
"""

class Index(webapp2.RequestHandler):
    def get(self):
        edit_header = "<h1>Signup</h1>"

        table_form = """
        <form action='/signup-verification' method="post">
        <tbody>
            <tr>
                <td>
                    <label for = "username">Username</label>
                </td>
                <td>
                    <input type="text" name="username" value required/>
                    <span class="error"></span>
                </td>
            </tr>
            <br>

            <tr>
                <td>
                    <label for = "password">Password</label>
                </td>
                <td>
                    <input type="password" name="password" required/>
                    <span class="error"></span>
                </td>
            </tr>
            <br>

            <tr>
                <td>
                    <label for = "verify_password">Verify Password</label>
                </td>
                <td>
                    <input type="password" name="verify_password" required/>
                    <span class="error"></span>
                </td>
            </tr>
            <br>

            <tr>
                <td>
                    <label for = "email">Email (optional)</label>
                </td>
                <td>
                    <input type="text" name="email" required/>
                    <span class="error"></span>
                </td>
            </tr>
            <br>

            <input type = "submit"/>
            </form>
            """

        error = self.request.get("error")

        username = self.request.get("username")
        password = self.request.get("password")
        verify_password = self.request.get("verify_password")
        email = self.request.get("email")

        if error:
            error_esc = cgi.escape(error, quote=True)
            error_element = '<p class="error">' + error_esc + '</p>'
        elif username:
            error_esc = cgi.escape(username, quote=True)
            error_element = '<p class="error">' + error_esc + '</p>'
        elif password:
            error_esc = cgi.escape(password, quote=True)
            error_element = '<p class="error">' + error_esc + '</p>'
        elif email:
            error_esc = cgi.escape(username, quote=True)
            error_element = '<p class="error">' + error_esc + '</p>'
        else:
            error_element = ''


        content = table_form + error_element
        self.response.write(edit_header + content)


class Signup_Verification(webapp2.RequestHandler):
    def post(self):
        entered_username = self.request.get("username")
        entered_password = self.request.get("password")
        entered_password2 = self.request.get("verify_password")
        entered_email = self.request.get("email")

        #validating username input - blank username
        if entered_username == "":
            error = "Please enter a username!"
            self.redirect("/?error=Please enter a username!")

        #validating username input - username contains prohibited characters
        validated_username = valid_username(entered_username)
        if not validated_username:
            error = "Please enter a valid username!"
            self.redirect("/?error=Please enter a valid username!")

        #validating password and verify_password user inputs - entered passwords do not match
        if entered_password != entered_password2:
            error = "Your passwords do not match!"
            self.redirect("/?error=Your passwords do not match!")

        #validating email input - email contains prohibited characters
        validated_email = valid_email(entered_email)
        if not validated_email:
            error = "Please enter a valid email!"
            self.redirect("/?error=Please enter a valid email!")

        #else:
            #self.redirect("/?welcome")


        content = page_header + "<p>" + "Welcome, " + entered_username + "!" + "</p>" + page_footer
        self.response.write(content)

#Do I need the following class given I am printing the desired content above?
class Welcome(webapp2.RequestHandler):
    def post(self):
        validated_username = self.request.get("username")
        escaped_username = cgi.escape(validated_username, quote=True)
        welcome_message = "Welcome, " + escaped_username + "!"

        content = page_header + "<p>" + welcome_message + "</p>" + page_footer
        self.response.write(welcome_message)

app = webapp2.WSGIApplication([
    ('/', Index),
    ('/signup-verification', Signup_Verification),
    ('/welcome', Welcome)],
    debug=True)
