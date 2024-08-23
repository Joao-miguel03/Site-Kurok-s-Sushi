from flask import Blueprint, render_template

adm_route = Blueprint('adm',__name__)

@adm_route.route('/') 
def home():
    pass
