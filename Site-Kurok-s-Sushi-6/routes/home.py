from flask import Blueprint, render_template, request, redirect, jsonify, url_for
from banco_dados.database import get_db

home_route = Blueprint('home', __name__)

@home_route.route("/")
def home():
    return render_template("index.html", logado = False)

@home_route.route('/menu/<int:id>')
def menu(id):
    return render_template('menu.html', id_pessoa = id)

# para logar
@home_route.route('/login', methods = ["GET", "POST"])
def logar():
    if request.method == "POST":

        kuro_database = get_db()
        cursor = kuro_database.cursor()

        req = request.form

        percorrer_clientes = cursor.execute('select * from cliente').fetchall()
        kuro_database.commit()

        # consegui ajeitar a parte do login, por enquanto é só essa parte
        if percorrer_clientes != []:
            for i in percorrer_clientes:
                if str(i[1]) == req['nome']:
                    if str(i[2]) == req['email']:
                        if str(i[3]) == req['senha']:
                            pessoa = i
                            return render_template('index.html', pessoa = pessoa, logado = True)
            return jsonify({'error': 'Não está cadastrado'})
        else:
            return redirect('/data/form')

    return render_template("login.html")

@home_route.route('/data')
def adm():
    return render_template('adm.html')
    

@home_route.route('/config')
def configuracoes():
    return render_template('configuracao.html')