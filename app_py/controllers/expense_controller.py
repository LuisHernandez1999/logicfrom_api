from flask import request, jsonify
from app_py.service.exepense_service import (
    create_expend_service,
    get_total_expenses_service,
    get_highest_expense_service,
    get_category_with_highest_expense_service,
    get_expenses_count_by_category_service,
    get_category_with_lowest_expense_service
)

from app_py.controllers.user_controller import get_user_from_token  



def insert_expense_controller():
  
    try:
        data = request.get_json()  
        print(f"[INFO] Iniciando processo de inserção de gasto com dados: {data}")
        
     
        id_user = data.get('id_user')

        if not id_user:
         
            id_user = get_user_from_token()
            if not id_user:
                return jsonify({"erro": "Token inválido ou ausente. Por favor, faça login."}), 401
        
       
        data['id_user'] = id_user
        
       
        result, status = create_expend_service(data)
        
        print(f"[INFO] Gasto inserido com sucesso: {result}")
        return jsonify(result), status
    except Exception as e:
        print(f"[ERRO] Falha ao processar inserção de gasto: {e}")
        return jsonify({"erro": "Erro interno no servidor"}), 500

def get_total_expenses_controller():
   
    try:
        print("[INFO] Iniciando processo para calcular o total de gastos")
        
        result, status = get_total_expenses_service()
        
        print(f"[INFO] Total de gastos calculado: {result}")
        return jsonify(result), status
    except Exception as e:
        print(f"[ERRO] Falha ao calcular total de gastos: {e}")
        return jsonify({"erro": "Erro interno no servidor"}), 500

def get_highest_expense_controller():
 
    try:
        print("[INFO] Iniciando processo para buscar o maior gasto")
        
        result, status = get_highest_expense_service()
        
        print(f"[INFO] Maior gasto encontrado: {result}")
        return jsonify(result), status
    except Exception as e:
        print(f"[ERRO] Falha ao buscar maior gasto: {e}")
        return jsonify({"erro": "Erro interno no servidor"}), 500

def get_category_with_highest_expense_controller():
    
    try:
        print("[INFO] Iniciando processo para buscar categoria com maior gasto")
        
        result, status = get_category_with_highest_expense_service()
        
        print(f"[INFO] Categoria com maior gasto encontrada: {result}")
        return jsonify(result), status
    except Exception as e:
        print(f"[ERRO] Falha ao buscar categoria com maior gasto: {e}")
        return jsonify({"erro": "Erro interno no servidor"}), 500

def get_expenses_count_by_category_controller():
  
    try:
        print("[INFO] Iniciando processo para buscar contagem de gastos por categoria")
        
        result, status = get_expenses_count_by_category_service()
        
        print(f"[INFO] Contagem de gastos por categoria: {result}")
        return jsonify(result), status
    except Exception as e:
        print(f"[ERRO] Falha ao buscar contagem de gastos por categoria: {e}")
        return jsonify({"erro": "Erro interno no servidor"}), 500

def get_category_with_lowest_expense_controller():
  
    try:
        print("[INFO] Iniciando processo para buscar categoria com menor gasto")
        
        result, status = get_category_with_lowest_expense_service()
        
        print(f"[INFO] Categoria com menor gasto encontrada: {result}")
        return jsonify(result), status
    except Exception as e:
        print(f"[ERRO] Falha ao buscar categoria com menor gasto: {e}")
        return jsonify({"erro": "Erro interno no servidor"}), 500
