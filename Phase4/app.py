from flask import Flask, render_template, request , redirect , url_for

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/feedback', methods=['GET','POST'])
def form():
    if request.method=="POST":
        name= request.form.get('username')
        message= request.form.get('message')
        return redirect(url_for("thankyou"))
    return render_template('feedback.html')
@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')
