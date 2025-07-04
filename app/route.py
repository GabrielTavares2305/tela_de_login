from app import app
from flask import render_template, url_for

@app.route('/')
def homepage():
    usuario = 'DataPrev'
    email = 'gabriel@dataprev.com'
    context = {
        'usuario': usuario,
        'email': email
    }

    return render_template('index.html', context=context)



@app.route('/login/')
def loginpage():
    return render_template('login.html')