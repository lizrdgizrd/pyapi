#!/usr/bin/python3

from flask import Flask, make_response, request, render_template
import datetime

app = Flask(__name__)

@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/setcookie", methods = ['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']

        resp = make_response(render_template("readcookie.html"))

        resp.set_cookie("userID", user)
        resp.set_cookie("date", str(datetime.datetime.now()))

        return resp

@app.route("/getcookie")
def getcookie():
    name = request.cookies.get("userID")
    time = request.cookies.get("date")
    return "<h1>Looks like your username is "+name+"</h1><h2>And you were here before at: "+time+"</h2>"

if __name__ == "__main__":
    app.run(port=5006)
