from flask import Blueprint
from app_py.controllers.user_controller import login_user, api_criar_user


user_routes = Blueprint('user_routes', __name__)


user_routes.route('/login', methods=['POST'])(login_user)


user_routes.route('/create_user', methods=['POST'])(api_criar_user)
