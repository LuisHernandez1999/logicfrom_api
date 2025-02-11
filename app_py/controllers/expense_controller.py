from flask import request, jsonify
from app_py.service.exepense_service import (
    create_expend_service,
    get_total_expenses_service,
    get_highest_expense_service,
    get_category_with_highest_expense_service,
    get_expenses_count_by_category_service,
    get_category_with_lowest_expense_service
)
from app_py.operations.repositories.expense_repository import get_expenses_data
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
        
        # passar id_user para o serviço
        id_user = request.args.get('id_user')  # obtém o id_user da URL
        if not id_user:
            return jsonify({"erro": "ID do usuário não fornecido."}), 400

        result, status = get_highest_expense_service(id_user)

        if status == 404:
            return jsonify({"erro": "Nenhum gasto encontrado."}), 404
        
        print(f"[INFO] Maior gasto encontrado: {result}")
        return jsonify(result), status
    except Exception as e:
        print(f"[ERRO] Falha ao buscar maior gasto: {e}")
        return jsonify({"erro": "Erro interno no servidor"}), 500

def get_category_with_highest_expense_controller():
    try:
        # Pegando o id_user da URL
        id_user = request.args.get('id_user')

        # Se id_user não for fornecido, tenta pegar do token (caso exista)
        if not id_user:
            id_user = get_user_from_token()  

        # Se id_user ainda não for encontrado, retorna erro
        if not id_user:
            return jsonify({"erro": "ID do usuário não encontrado. Por favor, forneça um ID de usuário válido ou faça login."}), 400
        
        print("[INFO] Iniciando processo para buscar categoria com maior gasto")
        
        # Chamando o serviço para obter a categoria com maior gasto
        result, status = get_category_with_highest_expense_service(id_user)
        
        print(f"[INFO] Categoria com maior gasto encontrada: {result}")
        return jsonify(result), status

    except Exception as e:
        print(f"[ERRO] Falha ao buscar categoria com maior gasto: {e}")
        return jsonify({"erro": "Erro interno no servidor"}), 500
    

def get_expenses_count_by_category_controller():
    try:
        # Pegando o id_user da URL
        id_user = request.args.get('id_user')

        # Se id_user não for fornecido, tenta pegar do token (caso exista)
        if not id_user:
            id_user = get_user_from_token()

        # Se id_user ainda não for encontrado, retorna erro
        if not id_user:
            return jsonify({"erro": "ID do usuário não encontrado. Por favor, forneça um ID de usuário válido ou faça login."}), 400

        print("[INFO] Iniciando processo para buscar contagem de gastos por categoria")

        # Passando o id_user para a função de serviço
        result, status = get_expenses_count_by_category_service(id_user)

        # Se o resultado for um erro, retorne o erro com o status adequado
        if isinstance(result, dict) and 'erro' in result:
            return jsonify(result), status

        print(f"[INFO] Contagem de gastos por categoria: {result}")
        return jsonify(result), status

    except Exception as e:
        print(f"[ERRO] Falha ao buscar contagem de gastos por categoria: {e}")
        return jsonify({"erro": "Erro interno no servidor"}), 500
    
def get_category_with_lowest_expense_controller():
    try:
        # Pegando o id_user da URL
        id_user = request.args.get('id_user')

        # Se id_user não for fornecido, tenta pegar do token (caso exista)
        if not id_user:
            id_user = get_user_from_token()  

        # Se id_user ainda não for encontrado, retorna erro
        if not id_user:
            return jsonify({"erro": "ID do usuário não encontrado. Por favor, forneça um ID de usuário válido ou faça login."}), 400
        
        print("[INFO] Iniciando processo para buscar categoria com menor gasto")
        
        # Passando o id_user para o serviço
        result = get_category_with_lowest_expense_service(id_user)
        
        print(f"[INFO] Categoria com menor gasto encontrada: {result}")
        return jsonify(result), 200

    except Exception as e:
        print(f"[ERRO] Falha ao buscar categoria com menor gasto: {e}")
        return jsonify({"erro": "Erro interno no servidor"}), 500

def get_total_expenses_controller():
    
    try:
        print("[INFO] Iniciando processo para calcular o total de gastos")

        
        id_user = request.args.get('id_user') 

       
        if not id_user:
            id_user = get_user_from_token()  

    
        if not id_user:
            return jsonify({"erro": "ID do usuário não encontrado. Por favor, forneça um ID de usuário válido ou faça login."}), 400

      
        df, status_code = get_expenses_data(id_user)

       
        if df is None or df.empty:
            return jsonify({"erro": "Nenhum gasto encontrado."}), 404

       
        total_gastos = df['valor'].sum()

        return jsonify({
            "total_gastos": float(total_gastos)
        }), 200

    except Exception as e:
        print(f"[ERRO] Falha ao calcular total de gastos: {e}")
        return jsonify({"erro": "Erro interno no servidor"}), 500
    


def get_user_expenses_controller():
    try:
        print("[INFO] Iniciando processo para obter os gastos do usuário.")

        
        id_user = request.args.get('id_user')

      
        if not id_user:
            id_user = get_user_from_token()

      
        if not id_user:
            return jsonify({"erro": "ID do usuário não encontrado. Por favor, forneça um ID de usuário válido ou faça login."}), 400

        
        df, status_code = get_expenses_data(id_user)

       
        if df is None or df.empty:
            return jsonify({"erro": "Nenhum gasto encontrado para este usuário."}), 404

      
        expenses = []
        for _, row in df.iterrows():
            expenses.append({
                "id": row["id"],
                "id_user": row["id_user"],
                "nome": row["nome"],
                "data": row["data"].strftime("%Y-%m-%d") if row["data"] else None,
                "valor": float(row["valor"]),
                "categoria": row["categoria"]
            })

        return jsonify({"gastos": expenses}), 200

    except Exception as e:
        print(f"[ERRO] Falha ao obter gastos: {e}")
        return jsonify({"erro": "Erro interno no servidor."}), 500