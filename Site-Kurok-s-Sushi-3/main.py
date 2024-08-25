from flask import Flask
from routes.adm import adm_route
from routes.cardapio import cardapio_route
from routes.chat import chat_route
from routes.home import home_route
from routes.client import client_route

app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(client_route, url_prefix = '/cliente')
app.register_blueprint(cardapio_route, url_prefix = '/cardapio')
app.register_blueprint(chat_route, url_prefix = '/chat')
app.register_blueprint(adm_route, url_prefix = '/adm')

app.run(debug=True)