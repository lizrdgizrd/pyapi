#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
   return "Hello World"

@app.route("/rob")
def rob():
    return "Hello Rob\n"

if __name__ == "__main__":
   app.run(port=5006) # runs the application
