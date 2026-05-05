from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/feedback', methods=['GET','POST'])
def form():
    if request.method=="POST":
        name= request.form.get('username')
        message= request.form.get('message')
        return render_template('thankyou.html', username=name , message=message)
    return render_template('feedback.html')