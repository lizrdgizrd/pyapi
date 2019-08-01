#!/usr/bin/python3

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("hellobasic.html")

@app.route("/<username>")
def user_builder(username):
    return render_template("hellobasic2.html", coffee=username)

if __name__ == "__main__":
    app.run(port=5006)
