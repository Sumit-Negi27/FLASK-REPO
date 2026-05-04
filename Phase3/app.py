from flask import Flask , render_template ,request

app= Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login" ,methods =['GET','POST'])
def login():
    if request.method== "POST":
        username= request.form.get('username')
        password= request.form.get('password')
        print(username)
        print(password)
        if username=="sumit" and password=="123":
            return render_template("welcome.html")
        else:
            return "INVALID CREDENTIAL"
    return render_template("login.html")
