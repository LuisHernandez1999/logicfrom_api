from flask import Blueprint, request, jsonify
from app_py.controllers.expense_controller import (
    insert_expense_controller,
    insert_expense_controller,
    get_total_expenses_controller,
    get_highest_expense_controller,
    get_category_with_highest_expense_controller,
    get_expenses_count_by_category_controller,
    get_category_with_lowest_expense_controller,
)

expense_bp = Blueprint('expenses', __name__)
from app_py.controllers.user_controller import get_user_from_token

@expense_bp.route('/expenses', methods=['POST'])
def insert_expense():
    
    try:
       
        token = request.headers.get('Authorization').split(' ')[1]  
        user_data = get_user_from_token(token) 
        if not user_data:
            return jsonify({"erro": "Token inválido ou expirado"}), 401

       
        data = request.get_json()
        data['id_user'] = user_data['id_user']  # Associar o ID do usuário ao gasto

        print(f"[INFO] Recebendo requisição para inserir gasto: {data}")
        
        result, status = insert_expense_controller(data)
        
        print(f"[INFO] Resposta da inserção: {result}, Status: {status}")
        return jsonify(result), status
    except Exception as e:
        print(f"[ERRO] Falha ao processar requisição de inserção: {e}")
        return jsonify({"erro": "Erro interno no servidor"}), 500

@expense_bp.route('/expenses/total', methods=['GET'])
def get_total_expenses():
   
    try:
        print("[INFO] Requisição para obter total de gastos")
        
        result, status = get_total_expenses_controller()
        
        print(f"[INFO] Total de gastos calculado: {result}, Status: {status}")
        return jsonify(result), status
    except Exception as e:
        print(f"[ERRO] Falha ao calcular total de gastos: {e}")
        return jsonify({"erro": "Erro interno no servidor"}), 500

@expense_bp.route('/expenses/highest', methods=['GET'])
def get_highest_expense():
 
    try:
        print("[INFO] Requisição para obter o maior gasto")
        
        result, status = get_highest_expense_controller()
        
        print(f"[INFO] Maior gasto encontrado: {result}, Status: {status}")
        return jsonify(result), status
    except Exception as e:
        print(f"[ERRO] Falha ao buscar o maior gasto: {e}")
        return jsonify({"erro": "Erro interno no servidor"}), 500

@expense_bp.route('/expenses/category/highest', methods=['GET'])
def get_category_with_highest_expense():
  
    try:
        print("[INFO] Requisição para obter a categoria com maior gasto")
        
        result, status = get_category_with_highest_expense_controller()
        
        print(f"[INFO] Categoria com maior gasto: {result}, Status: {status}")
        return jsonify(result), status
    except Exception as e:
        print(f"[ERRO] Falha ao buscar categoria com maior gasto: {e}")
        return jsonify({"erro": "Erro interno no servidor"}), 500

@expense_bp.route('/expenses/count', methods=['GET'])
def get_expenses_count_by_category():
 
    try:
        print("[INFO] Requisição para obter a contagem de gastos por categoria")
        
        result, status = get_expenses_count_by_category_controller()
        
        print(f"[INFO] Contagem de gastos por categoria: {result}, Status: {status}")
        return jsonify(result), status
    except Exception as e:
        print(f"[ERRO] Falha ao buscar contagem de gastos por categoria: {e}")
        return jsonify({"erro": "Erro interno no servidor"}), 500

@expense_bp.route('/expenses/category/lowest', methods=['GET'])
def get_category_with_lowest_expense():

    try:
        print("[INFO] Requisição para obter a categoria com menor gasto")
        
        result, status = get_category_with_lowest_expense_controller()
        
        print(f"[INFO] Categoria com menor gasto: {result}, Status: {status}")
        return jsonify(result), status
    except Exception as e:
        print(f"[ERRO] Falha ao buscar categoria com menor gasto: {e}")
        return jsonify({"erro": "Erro interno no servidor"}), 500
