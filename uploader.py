#!/usr/bin/python3

from flask import Flask, render_template, request
from werkzeug import secure_filename

app = Flask(__name__)

@app.route("/upload")
def upload():
    return render_template("uploader.html")

@app.route("/uploader", methods = ["GET", "POST"])
def upload_file():
    if request.method == "POST":
        f = request.files["file"]
        f.save(secure_filename(f.filename))
        filecontent = "Don't mess with this file, yo.\n"
        with open(f.filename, "r") as theFile:
            filecontent += theFile.read()
        theFile.close()
        with open(f.filename, "w") as writeFile:
            writeFile.write(filecontent)
        writeFile.close()
        return "file uploaded successfully"

if __name__ == "__main__":
    app.run(port = 5006)
