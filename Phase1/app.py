from flask import Flask , request , Response , session , url_for , redirect

app=Flask(__name__)
app.secret_key="sus"#session ko lock krne ke liye taaki aur aur user access nah kr pae
#home page (login page)
@app.route("/", methods=["GET","POST"])
def login():
    if request.method =="POST":
        username=request.form.get("username")
        password=request.form.get("password")

        if username=="admin" and password=="123":
            session["user"]=username #store in session
            return redirect(url_for('welcome'))
        else:
            return Response("invalid username or password \n please try again")
    return '''
<!DOCTYPE html>
<html>
<head>
    <title>Login Page</title>
    <style>
        body {
            font-family: Arial;
            background: #f0f2f5;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .login-box {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px gray;
            width: 300px;
            text-align: center;
        }

        input {
            width: 90%;
            padding: 10px;
            margin: 8px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        input[type="submit"] {
            background: #007bff;
            color: white;
            border: none;
            cursor: pointer;
        }

        input[type="submit"]:hover {
            background: #0056b3;
        }
    </style>
</head>
<body>

    <div class="login-box">
        <h2>Login Page</h2>
        <form method="POST">
            <input type="text" name="username" placeholder="Enter Username">
            <input type="password" name="password" placeholder="Enter Password">
            <input type="submit" value="Login">
        </form>
    </div>

</body>
</html>
'''
#greeting route
@app.route("/welcome")
def welcome():
    if "user"  in session:
        return f'''
<!DOCTYPE html>
<html>
<head>
    <title>Welcome</title>
    <style>
        body {{
            font-family: Arial;
            background: linear-gradient(to right, #4facfe, #00f2fe);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }}

        .box {{
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0px 0px 15px rgba(0,0,0,0.2);
            text-align: center;
            width: 320px;
        }}

        h2 {{
            color: #333;
        }}

        a {{
            display: inline-block;
            margin-top: 15px;
            padding: 10px 20px;
            background: #ff4d4d;
            color: white;
            text-decoration: none;
            border-radius: 5px;
        }}

        a:hover {{
            background: #cc0000;
        }}
    </style>
</head>
<body>

    <div class="box">
        <h2>Welcome, {session["user"]}! 🎉</h2>
        <p>You have successfully logged in.</p>
        <a href="{url_for('logout')}">Logout</a>
    </div>

</body>
</html>
'''
    return redirect(url_for('login'))

#logout route
@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("login"))