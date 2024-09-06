from flask import Flask
from routes.cardapio import cardapio_route
from routes.chat import chat_route
from routes.home import home_route
from routes.cliente import cliente_route
from routes.carteira import carteira_route

app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(cardapio_route, url_prefix = '/cardapio')
app.register_blueprint(cliente_route, url_prefix = '/cliente')
app.register_blueprint(carteira_route, url_prefix = '/carteira')
app.register_blueprint(chat_route, url_prefix = '/chat')

app.run(debug=True)