from app import app
from flask import render_template, url_for,request

@app.route('/login')
def loginpage():
    return render_template('login.html')



@app.route('/home/')
def homepage():
    usuario = 'DataPrev'
    email = 'gabriel@dataprev.com'
    context = {
        'usuario': usuario,
        'email': email
    }

    return render_template('index.html', context=context)

@app.route('/cadastro/', methods=['GET','POST'])
def cadastro():
    context = {}
    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa')
        print('GET', pesquisa)
        context.update({'pesquisa' : pesquisa})
    if request.method == 'POST':
       nome = request.form['nome']
       email = request.form['email']
       cpf = request.form['cpf']





    return render_template('cadastro.html', context=context)



