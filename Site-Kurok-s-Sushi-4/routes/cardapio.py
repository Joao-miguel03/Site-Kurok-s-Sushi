from flask import Blueprint, render_template

cardapio_route = Blueprint('cardapio',__name__)

@cardapio_route.route('/') 
def home():
    pass
