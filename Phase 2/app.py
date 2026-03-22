from flask import Flask,redirect,url_for,Request,Response,session,render_template

app= Flask(__name__)

@app.route('/')
def home():
    return render_template("form.html")
@app.route("/submit", method=["POST"])
def login():
    return render_template("form.html")