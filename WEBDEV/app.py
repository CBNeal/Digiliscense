from flask import Flask, render_template, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

################
#Database config
################
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

################
#Database model 
################
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    bloodtype = db.Column(db.String(10), nullable = False)
    contact = db.Column(db.String(50), nullable = False)
    info = db.Column(db.String(200), nullable = True)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route("/")
def home():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get["name"]
    blood = request.form.get["blood"]
    contact = request.form.get["contact"]
    info = request.form.get["info"]
    
    #Validation
    if not name or blood or not contact:
        return "Please fill out all required fields.", 400
    #Save to database
    new_user = User(name = name, bloodtype = blood, contact = contact, info = info)
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for("user_list"))

@app.route("/user")
def user_list():
    users = user.query.all()
    return render_template("index.html", users = users)

####################################
if __name__ == '__main__':
    app.run(debug=True)
