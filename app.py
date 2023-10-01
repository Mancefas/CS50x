import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import inputs_validation
from apiCalls import weather_hourly

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///cycling.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    user = session["user_id"] if "user_id" in session else None

    # if there is user in session provide it to function
    if user:
        city = db.execute("SELECT city FROM user_preferences WHERE user_id = ?", user)[
            0
        ]["city"]
        data = weather_hourly(user, city)
        return render_template("index.html", data=data, city=city)
    else:
        data = weather_hourly()

    if data == "error":
        return render_template("index.html", error=data), 500

    return render_template("index.html", data=data)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # get all inputs
        email = request.form.get("email")
        passw = request.form.get("password")
        rePassw = request.form.get("rePassword")

        # check inputs with inputs validation function
        checkInputs = inputs_validation(email, passw, "register.html", rePassw)
        if checkInputs != None:
            return checkInputs

        # checking if email was used to register before
        userIsInDB = db.execute("SELECT username FROM users WHERE username = ?", email)
        if userIsInDB:
            return (
                render_template(
                    "register.html", emailErr=email + "is registered before."
                ),
                400,
            )

        # add user to database of users
        db.execute(
            "INSERT INTO users (username, hash) VALUES(?,?)",
            email,
            generate_password_hash(passw),
        )

        # get latest added user id
        result = db.execute("SELECT MAX(id) as max_id FROM users")
        user_id = result[0]["max_id"]

        # add user to user_preferences with default values
        db.execute("INSERT INTO user_preferences (user_id) VALUES (?)", user_id)

        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    # Forget any user_id
    session.clear()

    if request.method == "POST":
        # get inputs
        email = request.form.get("email")
        passw = request.form.get("password")

        # check inputs with inputs validation function
        checkInputs = inputs_validation(email, passw, "login.html")
        if checkInputs != None:
            return checkInputs

        # check for user in DB
        userFromDb = db.execute("SELECT * FROM users WHERE username = ?", email)

        # check if user exists and the password match
        if len(userFromDb) != 1:
            return render_template("login.html", userErrDb="User not found")
        if not check_password_hash(userFromDb[0]["hash"], passw):
            return render_template(
                "login.html", passErrDb="Invalid password", email=email
            )

        # add user id to session
        session["user_id"] = userFromDb[0]["id"]

        return redirect("/")
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    # clear user info from session
    session.clear()
    return redirect("/")


@app.route("/admin", methods=["GET", "POST"])
def admin():
    user = session["user_id"]
    data = db.execute(
        "SELECT low, mid, high, city FROM user_preferences WHERE user_id = ?", user
    )[0]
    preferences = {"low": data["low"], "mid": data["mid"], "high": data["high"]}
    city = data["city"]
    print(type(city))

    if request.method == "POST":
        # selecting all inputs
        submit = request.form.get("submit")
        abort = request.form.get("abort")
        low_value = request.form.get("low")
        low = int(low_value) if low_value is not None else None
        mid_value = request.form.get("mid")
        mid = int(mid_value) if mid_value is not None else None
        high_value = request.form.get("high")
        high = int(high_value) if high_value is not None else None

        geoInput = request.form.get("geoInput")

        if abort:
            return render_template("admin.html", preferences=preferences, city=city)
        elif submit:
            if low is not None and low != preferences["low"]:
                db.execute(
                    "UPDATE user_preferences SET low=? WHERE user_id=?", low, user
                )
                return redirect("/")
            elif mid is not None and mid != preferences["mid"]:
                db.execute(
                    "UPDATE user_preferences SET mid=? WHERE user_id=?", mid, user
                )
                return redirect("/")
            elif high is not None and high != preferences["high"]:
                db.execute(
                    "UPDATE user_preferences SET high=? WHERE user_id=?", high, user
                )
                return redirect("/")
            elif geoInput:
                db.execute(
                    "UPDATE user_preferences SET city=? WHERE user_id=?", geoInput, user
                )
                return redirect("/")
        return redirect("/")
    else:
        return render_template("admin.html", preferences=preferences, city=city)
