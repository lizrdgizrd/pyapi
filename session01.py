#!/usr/bin/python3

from flask import Flask, session, render_template, redirect, url_for, escape, request

app = Flask(__name__)

app.secret_key = "any random string"

@app.route("/")
def index():
    if "username" in session:
        username = session["username"]
        if "count" in session:
            session["count"] = str(int(session["count"])+1)
        else:
            session['count'] = 1
        return "Logged in as " + username + " for "+str(session['count'])+" times<br><b><a href = '/logout'>click here to log out</a></b>"
        

    return "You are not logged in <br><a href = '/login'></b>click here to log in</b></a>"


@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":

        session["username"] = request.form.get("username")
        return redirect(url_for("index"))

    return """<form action = "" method = "post"><p><input type = text name = username></p>
        <p><input type = submit value = Login></p></form>"""

@app.route("/logout")
def logout():
    # remove the username from the session if it is there
    session.pop("username", None)
    session.pop("count", None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(port=5006)
