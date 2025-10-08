from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

'''
@app.route('/submit', methods = ['POST'])
def submit():
    name = request.form['name']
    return f"hello {name}! Thanks for submitting the form"
'''
###This app route will provide the user information for when a nfc tag is scanned
@app.route('/test')
def test():
    return "This works" 


if __name__ == '__main__':
    app.run(debug=True)