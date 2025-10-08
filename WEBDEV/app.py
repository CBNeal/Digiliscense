from flask import Flask, render_template, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    bloodtype = db.Column(db.String(50))




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
    return f"Thanks {name}, your Digilicense has been registered! To display your information, add [/USER] to the end of this URL"



'''
@app.route('/')
def home():
    return render_template('index.html')
'''
'''
@app.route('/submit', methods = ['POST'])
def submit():
    name = request.form['name']
    return f"hello {name}! Thanks for submitting the form"
'''
###This app route will provide the user information for when a nfc tag is scanned
@app.route('/USER')
def test():
    return render_template("index.html") 


if __name__ == '__main__':
    app.run(debug=True)