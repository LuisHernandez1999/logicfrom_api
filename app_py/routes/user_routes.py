from flask import Blueprint
from app_py.controllers.user_controller import login_user, api_criar_user

# define o blueprint para as rotas de usuário
user_routes = Blueprint('user_routes', __name__)

# mapeia a rota de login
user_routes.route('/login', methods=['POST'])(login_user)

# Mapeia a rota de criação de usuário
user_routes.route('/create_user', methods=['POST'])(api_criar_user)
