from flask import Flask 

app=Flask(__name__)

@app.route("/")
def home():
    return "Hey Users! this is my first website"

@app.route("/about")
def about():
    return 'this page is about us'