from app import db

class Cadastro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=True)
    cpf = db.Column(db.Integer, nullable=True)

