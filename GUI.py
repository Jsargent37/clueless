from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta
#from Clue import Clue
import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
SERVER = ""
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

app = Flask(__name__)
app.secret_key = "super secret session key dont tell anyone"
app.permanent_session_lifetime = timedelta(hours=12)
parameters = []

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

@app.route("/", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        session["user"] = request.form["nm"]
        parameters.append("user")
        return redirect(url_for("startuppage"))
    else:
        if "user" in session:
            parameters.append("user")
            return redirect(url_for("startuppage"))
        else:
            return render_template("home.html")

@app.route("/startuppage", methods = ["GET", "POST"])
def startuppage():
    if "user" in session:
        if request.method == "POST":
            game_code = request.form["gc"]

            """
            needs to be an if statement of if gc is in the database
            add player to the database and the clue game
            if gc is not in database, create new clue game instance
            add clue game to the database and add player to clue game  and database
            """

            
            #found_gc = game.query.filter_by(room=game_code)
            #play = game(game_code[0])
            #db.session.add(play)
            #db.commit()

            session["gc"] = game_code
            parameters.append("gc")
            return redirect(url_for("pickcharacter"))
        else:
            return render_template("startuppage.html", user = session["user"])
    else:
        return redirect(url_for("login"))
    
@app.route("/pickcharacter", methods = ["GET", "POST"])
def pickcharacter():
    if "user" in session and "gc" in session:
        if request.method == "POST":
            session["pc"] = request.form["PC"]
            parameters.append("pc")
            
            """
            After picking player, user should be redirected to a waiting room
            which has a start button that appears only after 2 other users have
            joined that specific game. After hitting start button, they would 
            get redirected to the game board.
            """

            return redirect(url_for("waitingroom"))
        else:
            client.connect(ADDR)
            return render_template("pickcharacter.html", user = session["user"])
    elif "user" in session and "gc" not in session:
        return redirect(url_for("startuppage"))
    else:
        return redirect(url_for("login"))

@app.route("/waitingroom", methods = ["GET", "POST"])
def waitingroom():
    if "user" in session and "gc" in session and "pc" in session:
        if request.method == "POST":
            return redirect(url_for("board"))
        else:
            return render_template("waitingroom.html", user = session)
    elif "user" in session and "gc" in session and "pc" not in session:
        return redirect(url_for("pickcharacter"))
    elif "user" in session and "gc" not in session:
        if "pc" in session:
            session.pop("pc")
        return redirect(url_for("startuppage"))
    else:
        if "pc" in session and "gc" in session:
            session.pop("pc")
            session.pop("gc")
        return redirect(url_for("login"))

@app.route("/board")
def board():
    gc = session["gc"]
    user = session["user"]
    pc = session["pc"]
    
    #session["hand"] = newGame.set_players
    #newGame = session["newGame"]
    
    return(render_template("board.html", pc = pc, gc = gc, user = user))

@app.route("/logout")
def logout():
    for i in parameters:
        session.pop(i)
    parameters.clear()
    send(DISCONNECT_MESSAGE)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug = True)