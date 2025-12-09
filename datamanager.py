import json

# Get data from the json 'data/' folder.
def getData(path):
    file = open(f"data/{path}")
    data = json.loads(file.read())
    file.close()
    return data

# Get the list of users.
def getUsers():
    return getData("users.json")["list"]

# Get the data for a user.
def getUser(name):
    for user in getUsers():
        if user["username"] == name:
            return user

# Add a user, checking to verify none of the inputs violate the restrictions.
usernameallowed = "abcdefghijklmnopqrstuvwxyz1234567890-_"
displayallowed = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "
def addUser(display, username, password, password2):
    users = getUsers()
    if display == "" or username == "" or password == "" or password2 == "":
        return "Ever field must be filled."
    if not password == password2:
        return "Both passwords must match."
    for user in users:
        if user["display"] == display:
            return "Display name already taken."
    for user in users:
        if user["username"] == username:
            return "Username already taken."
    for character in username:
        if not character in usernameallowed:
            return "Username must only contain the following characters:\nabcdefghijklmnopqrstuvwxyz\n1234567890\n-_"
    for character in display:
        if not character in displayallowed:
            return "Display name must only contain the following characters:\nABCDEFGHIJKLMNOPQRSTUVWXYZ\nabcdefghijklmnopqrstuvwxyz\nSpaces"
    users.append({
        "display": display,
        "username": username,
        "password": password,
        "permissions": []
    })
    file = open(f"data/users.json", 'w')
    json.dump({"list": users}, file)
    file.close()
    return signin(username, password)