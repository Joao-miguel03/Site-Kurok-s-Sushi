from flask import Blueprint, render_template
home_route = Blueprint('home', __name__)

@home_route.route("/")
def home():
    return render_template("index.html")


@home_route.route('/login')
def logar():
    pass
    
@home_route.route('/cadastro', methods = ['POST'])
def cadastrar():
    pass

@home_route.route('/config')
def configuracoes():
    pass