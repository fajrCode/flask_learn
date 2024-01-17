from app import app
from app.controller import UserCtrl
from flask import render_template

@app.route("/")
def index():
    # return response.successMsg('API ready to use')
    return render_template("index.html", title="Flask and Jinja")

@app.route('/register', methods=["POST"])
def register():
    return UserCtrl.register()

@app.route("/login", methods=["POST"])
def login():
    return UserCtrl.login()
     