from flask import render_template, Blueprint

client_route = Blueprint('cliente', __name__)

@client_route.route('/login', methods = ['GET'])
def logar():
    return render_template("login.html")
    
@client_route.route('/cadastro', methods = ['POST'])
def cadastrar():
    pass

