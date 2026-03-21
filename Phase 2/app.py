from flask import Flask,redirect,url_for,Request,Response,session,render_template

app= Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")
