from flask import Blueprint, render_template, request, redirect
from app.controller import UserCtrl

Main = Blueprint('main', __name__, template_folder="..templates")

@Main.route('/')
def index():
    return render_template("index.html", title="Flask and Jinja")

@Main.route('/register', methods=["GET", "POST"])
def register():
    nameType = [
        {"type": "text", "name":"name", "text": "Name"},
        {"type": "email", "name":"email", "text": "Email"},
        {"type": "password", "name":"password", "text": "Password"},
        {"type": "password", "name":"confirmPassword", "text": "Confirm Password"}
    ]
    if request.method == "GET":
        return render_template('register.html', title="Register", nameType=nameType)
    else:
        UserCtrl.register()
        return redirect("/login")

@Main.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html', title="Login")
    else:
        UserCtrl.login()
        return "halaman dasboard"
