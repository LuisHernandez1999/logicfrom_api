import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app_py.database.db import criar_tabela_user
from flask import Flask
from app_py.controllers.user_controller import api_criar_user, login_user 
from app_py.routes.user_routes import user_routes
from app_py.controllers.expense_controller import (
    insert_expense_controller,
    get_total_expenses_controller,
    get_highest_expense_controller,
    get_category_with_highest_expense_controller,
    get_expenses_count_by_category_controller,
    get_category_with_lowest_expense_controller,
    get_user_expenses_controller
)


criar_tabela_user()


app = Flask(__name__)


app.register_blueprint(user_routes, url_prefix='/api')


app.add_url_rule('/criar_user', 'criar_user', api_criar_user, methods=['POST'])
app.add_url_rule('/login', 'login_user', login_user, methods=['POST'])


app.add_url_rule('/api/expenses', 'insert_expense', insert_expense_controller, methods=['POST'])
app.add_url_rule('/api/expenses/total', 'get_total_expenses', get_total_expenses_controller, methods=['GET'])
app.add_url_rule('/api/expenses/highest', 'get_highest_expense', get_highest_expense_controller, methods=['GET'])
app.add_url_rule('/api/expenses/category/highest', 'get_category_with_highest_expense', get_category_with_highest_expense_controller, methods=['GET'])
app.add_url_rule('/api/expenses/count', 'get_expenses_count_by_category', get_expenses_count_by_category_controller, methods=['GET'])
app.add_url_rule('/api/expenses/category/lowest', 'get_category_with_lowest_expense', get_category_with_lowest_expense_controller, methods=['GET'])
app.add_url_rule('/api/user/expenses', 'get_user_expenses', get_user_expenses_controller, methods=['GET'])

if __name__ == '__main__':
    app.run(debug=True)
