from flask import Flask, render_template, send_from_directory, url_for, request, make_response
import os.path
from datetime import datetime, timezone

import datamanager
import chat
from auth import signin, render_template_auth

app = Flask(__name__)

# Get readable time from timestamp.
@app.template_filter('fromutc')
def fromutc(utc):
    return datetime.fromtimestamp(utc).strftime("%I:%M%P")

# Return a page.
def get_page():
    try:
        if request.path.split("/")[1] == "":
            return "home"
        return request.path.split("/")[1]
    except:
        pass
    return "home"
app.jinja_env.globals.update(get_page=get_page)

# Return all of the channels.
def get_channels():
    selected = "Welcome"
    try:
        selected = request.cookies.get("channel")
    except:
        pass
    channels = chat.getChannels()
    for channel in channels:
        if channel["name"] == selected:
            channel["selected"] = True
    return channels
app.jinja_env.globals.update(get_channels=get_channels)

# Return the selected channel based on the cookie.
def get_channel():
    try:
        return chat.getChannel(request.cookies.get("channel"))
    except:
        response = make_response(chat.getChannel("Welcome"))
        response.set_cookie("channel", "Welcome")
        return chat.getChannel("Welcome")
app.jinja_env.globals.update(get_channel=get_channel)

# Get a list of users.
def get_users():
    return datamanager.getUsers()
app.jinja_env.globals.update(get_users=get_users)

# Get the data for a specific user.
def get_user(user):
    return datamanager.getUser(user)
app.jinja_env.globals.update(get_user=get_user)

# Home page.
@app.route("/")
def index():
    return render_template('main/home.html')

# Chat page (only return if signed in).
@app.route("/chat")
def tool_chat():
    response = make_response(render_template_auth('tools/chat.html'))
    try:
        request.cookies.get("channel")
    except:
        response.set_cookie("channel", "Welcome")
    return response

# Calendar page.
@app.route("/calendar")
def tool_calendar():
    return render_template_auth('tools/calendar.html')

# Taskboard page.
@app.route("/taskboard")
def tool_taskboard():
    return render_template_auth('tools/taskboard.html')

# Account page.
@app.route("/account")
def tool_account():
    return render_template_auth('tools/account.html')

@app.route("/")

@app.route("/<path>")
def other_page(path):
    try:
        if os.path.isfile('templates/main/' + path + '.html'):
            return render_template('main/' + path + '.html')
    except:
        pass
    return "404: Page not found"


# Attempt to sign in the user.
@app.route("/api/signin")
def api_signin():
    try:
        return signin(request.headers["username"], request.headers["password"])
    except:
        return "Unknown Error."

# Attempt to sign up the user.
@app.route("/api/signup")
def api_signup():
    # try:
    return datamanager.addUser(request.headers["display"], request.headers["username"], request.headers["password"], request.headers["password2"])
    # except:
    #     return "Unknown Error."


# Start the application on port 80 (standard HTTP, requires root permissions).
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)