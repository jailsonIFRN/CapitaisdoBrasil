from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#------ ROTAS DO ARQUIVO da base.html --------

@app.route("/pagina_inicial")
def pagina_inicial():
    return render_template('pagina_inicial.html')

@app.route("/nordeste")
def nordeste():
    return render_template('nordeste.html')

@app.route("/sul")
def sul():
    return render_template('sul.html')

@app.route("/sudeste")
def sudeste():
    return render_template('sudeste.html')

@app.route("/centro_oeste")
def centro_oeste():
    return render_template('centro-oeste.html')





if __name__ == '__main__':
    app.run(debug=True)


# -----------------------------------------------------------

# @app.route("/cadastre_se")
# def cadastre_se():
#     return render_template('cadastre_se.html')

# @app.route('/cadastro', methods=['GET', 'POST'])
# def cadastro():
#     if request.method == 'POST':
#         # Aqui você pode processar os dados do formulário
#         nome = request.form['nome']
#         senha = request.form['senha']
#         # Adicione código para salvar os dados no banco de dados ou processá-los conforme necessário
#         return redirect(url_for('index'))
#     return render_template('cadastre_se.html')



# # --------------------------------------------------------------------
# @app.route('/cadastre')
# def cadastre():
#     return render_template('cadastrou.html')

# @app.route('/base', methods=['GET', 'POST'])
# def base():
#     return redirect(url_for('cadastro'))
#     return render_template('base.html')