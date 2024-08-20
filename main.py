from flask import Flask, render_template
import os.path

app = Flask(__name__)

links = {
    "coming-soon" : "comingSoon.html",

    "mintmc" : "mintmc.html"
}

@app.route("/")
def index():
    return render_template('home/index.html')

@app.route("/<path>")
def other_page(path):
    if os.path.isfile('templates/home/' + links.get(path)):
        return render_template('home/' + links.get(path))
    return "File not found"

if __name__ == "__main__":
    context = ("ssl/local.crt", "ssl/local.key")
    app.run(debug=True, host="0.0.0.0", port=5000, ssl_context=context)