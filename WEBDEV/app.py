from flask import Flask, render_template, request, redirect, url_for
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

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def register():
    # Debug print
    print("FORM DATA RECEIVED:", request.form)

    # Grab values from the form
    name = request.form.get("name", "").strip()
    blood = request.form.get("blood", "").strip()
    contact = request.form.get("contact", "").strip()
    info = request.form.get("info", "").strip()
    
    #Validation
    if not name or blood or not contact:
        return "Please fill out all required fields.", 400
    #Save to database
    new_user = User(name = name, bloodtype = blood, contact = contact, info = info)
    db.session.add(new_user)
    db.session.commit()

    print(f"✅ Saved user: {name}, {blood}, {contact}, {info}")

    return redirect(url_for("user_list"))

@app.route("/USER")
def user_list():
    users = user.query.all()
    return render_template("index.html", users = users)

####################################
if __name__ == '__main__':
    print("✅ Flask app started successfully (Digilicense)")
    app.run(debug=True)
