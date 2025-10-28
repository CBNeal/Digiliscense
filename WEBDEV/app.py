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
    pin = db.Column(db.String(6), nullable = False)
    name = db.Column(db.String(50), nullable = False)
    bloodtype = db.Column(db.String(10), nullable = False)
    contact = db.Column(db.String(50), nullable = False)
    info = db.Column(db.String(200), nullable = True)

with app.app_context():
    db.create_all()
## This is for the "homebase", opening page - C
@app.route("/")
def home():
    return render_template("register.html")

#Access user info by PIN
@app.route("/access", methods=["POST"])
def access():
    pin = request.form['pin'].strip()
    user = User.query.filter_by(pin=pin).first()

    if user:
        return render_template("user.html", user=user)
    else:
        return "❌ Invalid PIN. User not found.", 404

@app.route("/register", methods=["POST"])
def register():
    # Debug print
    print("FORM DATA RECEIVED:", request.form)

    # Grab and strip form fields
    pin = request.form.get("pin", "").strip()
    name = request.form.get("name", "").strip()
    blood = request.form.get("blood", "").strip()
    contact = request.form.get("contact", "").strip()
    info = request.form.get("info", "").strip()

    # Validation
    if not name or not blood or not contact:
        return "Please fill out all required fields., User will not work properly if all fields are not filled", 400

    # Save to database
    new_user = User(name = name, pin = pin,  bloodtype = blood, contact = contact, info = info)
    db.session.add(new_user)
    db.session.commit()

    print(f"✅ Saved user: {name}, {pin}, {blood}, {contact}, {info}, User saved into SQLITE file")

    return redirect(url_for("user_list"))


@app.route('/user/<int:user_id>')
def get_user(user_id):
    user = User.query.filter_by(pin=pin).first()

    if user:
        return render_template('user.html', user=user)
    else:
        return f"User with ID {user_id} not found. Check again and see if the Code on the DIGILISCENSE is correct", 404

### For showcasing the user  page 
@app.route("/USER")
def user_list():
    users = User.query.all()
    return render_template("index.html", users = users)

####################################
if __name__ == '__main__':
    print("✅ Flask app started successfully (Digilicense)")
    app.run(debug=True)
