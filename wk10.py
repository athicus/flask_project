from flask import Flask, url_for, redirect
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello and <b>Happy Holidays</b>"

@app.route("/python")
def hello_python():
    return "Hello Python"

@app.route("/greetings/<holiday>")
def hello_greeting(holiday):
    if greeting == "christmas":
        return redirect(url_for("Merry Chirstmas"))
    else:
        return redirect(url_for("Happy New Years"))

@app.route("/admin")
def hello_admin():
    return "Hello Admin"

@app.route("/guest/<guest>")
def hello_guest(guest):
    return "Hello {0} as Guest".format(guest)

if __name__ == "__main__":
    app.run()
