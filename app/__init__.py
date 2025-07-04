from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODOFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.route import loginpage 
from app.models import Cadastro