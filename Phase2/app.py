from flask import Flask, redirect, url_for ,request,Response,session,render_template

app= Flask(__name__)

@app.route('/')
def login():
    return render_template("form.html")
@app.route("/submit", methods=["POST"])
def submit():
    username=request.form.get("username")
    password=request.form.get("password")
    users={'sumit':'123', 'sum':'12345','admin':'000'}
    if username in users and password==users[username]:
        return render_template("welcome.html" ,username=username)
    else:
        return render_template("welcome2.html" ,username=username)