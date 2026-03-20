from flask import Flask ,request

app=Flask(__name__)

@app.route("/")
def home():
    return "Hey Users! this is my first website"

@app.route("/about")
def about():
    return 'this page is about us'

@app.route("/submit",methods=["GET","POST"])
def submit():
    if request.method=="POST":
        return 'u send something'
    else:
        return 'u just visiting website'