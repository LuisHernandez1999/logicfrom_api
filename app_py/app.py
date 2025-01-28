import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app_py.database.db import criar_tabela_user
from flask import Flask
from app_py.controllers.user_controller import api_criar_user, login_user
from app_py.routes.user_routes import user_routes

# crie a tabela de usuários, caso não exista
criar_tabela_user()

app = Flask(__name__)

app.register_blueprint(user_routes, url_prefix='/api')

app.add_url_rule('/criar_user', 'criar_user', api_criar_user, methods=['POST'])
app.add_url_rule('/login', 'login_user', login_user, methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True)
