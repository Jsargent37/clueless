from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from Clue import Clue

app = Flask(__name__)
app.secret_key = "super secret key dont tell anyone"
app.permanent_session_lifetime = timedelta(hours=12)
parameters = []

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class game(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    room_id = db.Column(db.String(100))
    player1 = db.Column(db.Boolean)
    x1 = db.Column(db.Integer)
    y1 = db.Column(db.Integer)
    player2 = db.Column(db.Boolean)
    x2 = db.Column(db.Integer)
    y2 = db.Column(db.Integer)
    player3 = db.Column(db.Boolean)
    x3 = db.Column(db.Integer)
    y3 = db.Column(db.Integer)
    player4 = db.Column(db.Boolean)
    x4 = db.Column(db.Integer)
    y4 = db.Column(db.Integer)
    player5 = db.Column(db.Boolean)
    x5 = db.Column(db.Integer)
    y5 = db.Column(db.Integer)
    player6 = db.Column(db.Boolean)
    x6 = db.Column(db.Integer)
    y6 = db.Column(db.Integer)

def __init__ (self, room):
        #unique room ID
        self.room_id = room
        #Ms. Scarlet
        self.player1 = False
        self.x1 = 0
        self.y1 = 3
        #Col Mustard
        self.player2 = False
        self.x2 = 1
        self.y2 = 4
        #Mr. White
        self.player3 = False
        self.x3 = 4
        self.y3 = 3
        #Mr. Green
        self.player4 = False
        self.x4 = 4
        self.y4 = 1
        #Ms. Peacock
        self.player5 = False
        self.x5 = 3
        self.y5 = 0
        #Prof. Plum
        self.player6 = False
        self.x6 = 1
        self.y6 = 0

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
            return redirect(url_for("board"))
        else:
            return render_template("pickcharacter.html", user = session["user"])
    elif "user" in session and "gc" not in session:
        return redirect(url_for("startuppage"))
    else:
        return redirect(url_for("login"))

@app.route("/board")
def board():
    gc = session["gc"]
    user = session["user"]
    pc = session["pc"]
    
    newGame = Clue([user, "Rylee", "Michelle"])

    return(render_template("board.html", pc = pc, gc = gc, user = user))

@app.route("/logout")
def logout():
    for i in parameters:
        session.pop(i)
    parameters.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug = True)