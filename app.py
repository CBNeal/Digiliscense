from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def register():
    name = request.form["name"]
    blood = request.form["blood"]
    contact = request.form["contact"]
    info = request.form["info"]
    
    print(f"Name: {name}, Blood: {blood}, Contact: {contact}, Info: {info}")

    return f"Thanks {name}, your Digilicense has been registered!"
