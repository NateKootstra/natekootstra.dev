from flask import request, render_template, make_response

import datamanager

# Sign in the user.
def signin(username, password):
    response = make_response("INVALID")
    for user in datamanager.getUsers():
        if user["username"] == username and user["password"] == password:
            response = make_response(f"OK")
            response.set_cookie("username", user["username"])
            response.set_cookie("password", user["password"])
    return response

# Check to see if the user is signed in.
def auth():
    try:
        for user in datamanager.getUsers():
            if user["username"] == request.cookies["username"] and user["password"] == request.cookies["password"]:
                return True
    except:
        pass
    return False

# Render the HTML template if the user is signed in.
def render_template_auth(file):
    if auth():
        return render_template(file)
    else:
        response = make_response(render_template("signin.html"))
        response.delete_cookie("username")
        response.delete_cookie("password")
        return response