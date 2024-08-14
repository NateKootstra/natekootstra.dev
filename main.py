from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('home/index.html')

if __name__ == "__main__":
    context = ("ssl/local.crt", "ssl/local.key")
    app.run(debug=True, host="0.0.0.0", port=5000, ssl_context=context)