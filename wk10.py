from flask import Flask, url_for, redirect
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello and <b>Happy Holidays</b>"

@app.route("/christmas")
def christmas_greeting():
    return "Merry Christmas"    

@app.route("/newyear")
def newyear_greeting():
    return "Happy New Year"

@app.route("/greetings/<holiday>")
def hello_greeting(holiday):
    if holiday == "christmas":
        return redirect(url_for("christmas_greeting"))
    else:
        return redirect(url_for("newyear_greeting"))

if __name__ == "__main__":
    app.run()
