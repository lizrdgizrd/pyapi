#!/usr/bin/Python3

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/scoretest/<int:score>")
def passfail(score):
    return render_template("highscore.html", marks = score)

if __name__ == "__main__":
    app.run(port=5006)