from app import app
from flask import render_template, url_for

@app.route('/')
def homepage():
    return 'Home'



@app.route('/login')
def loginpage():
    return render_template('index.html')