from flask import Flask, render_template, request, redirect, url_for

from database import db
import os
from flask_migrate import Migrate
from diario import Diario



app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
mydb = os.getenv('DB_DATABASE')

conexao = f"mysql+pymysql://{username}:{password}@{host}/{mydb}"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao


db.init_app(app)
migrate = Migrate(app, db)

@app.route('/add_diario')
def add_diario():
    d = Diario('LIC001', 'Desenvolvimento web')
    db.session.add(d)
    db.session.commit()
    return 'Dados inseridos com suceso!'


@app.route('/')
def index():
    return render_template('index.html')

#------ ROTAS DO ARQUIVO da base.html --------

@app.route("/pagina_inicial")
def pagina_inicial():
    return render_template('pagina_inicial.html')

@app.route("/cadastrar_capitais")
def cadastrar_capitais():
    return render_template('cadastrar_capitais.html')

@app.route("/fala_conosco")
def fale_conosco():
    return render_template('fale_conosco.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/buscar")
def buscar():
    return render_template('buscar.html')



if __name__ == '__main__':
    app.run(debug=True)

