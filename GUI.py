from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "super secret key dont tell anyone"
app.permanent_session_lifetime = timedelta(hours=12)
parameters = []

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
        return render_template("home.html")

@app.route("/startuppage", methods = ["GET", "POST"])
def startuppage():
    if "user" in session:
        if request.method == "POST":
            session["gc"] = request.form["gc"]
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
            return redirect(url_for("game"))
        else:
            return render_template("pickcharacter.html", user = session["user"])
    elif "user" in session and "gc" not in session:
        return redirect(url_for("startuppage"))
    else:
        return redirect(url_for("login"))

@app.route("/game")
def game():
    gc = session["gc"]
    user = session["user"]
    pc = session["pc"]
    return f"<h1> game: {gc} {user} {pc} </h1>"

@app.route("/logout")
def logout():
    for i in parameters:
        session.pop(i)
    parameters.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug = True)