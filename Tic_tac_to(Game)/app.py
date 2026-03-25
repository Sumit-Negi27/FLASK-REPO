from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "tictactoe"


def check_winner(board, player):
    win = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for i in win:
        if board[i[0]] == board[i[1]] == board[i[2]] == player:
            return True
    return False


@app.route("/")
def home():

    if "board" not in session:
        session["board"] = ["" for _ in range(9)]
        session["player"] = "X"
        session["winner"] = ""

    return render_template(
        "index.html",
        board=session["board"],
        player=session["player"],
        winner=session["winner"]
    )


@app.route("/move/<int:pos>")
def move(pos):

    board = session["board"]
    player = session["player"]

    if board[pos] == "" and session["winner"] == "":
        board[pos] = player

        if check_winner(board, player):
            session["winner"] = player
        else:
            session["player"] = "O" if player == "X" else "X"

    session["board"] = board
    return redirect("/")


@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)