from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/cardapio")
def cardapio():
    return render_template('cardapio.html')

@app.route("/cadastre_se")
def cadastre_se():
    return render_template('cadastre_se.html')
