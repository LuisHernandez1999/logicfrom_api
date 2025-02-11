from app_py.operations.repositories.expense_repository import insert_expense, get_expenses_count_by_category, get_highest_expense, get_expenses_data, get_category_with_highest_expense, get_category_with_lowest_expense,get_user_expenses
from flask import request, jsonify

def create_expend_service(data):
    try:
        nome = data.get('nome')
        data_gasto = data.get('data')  
        valor = data.get('valor')
        categoria = data.get('categoria')
        id_user = data.get('id_user')

        
        if not all([nome, valor, categoria, id_user]):
            return {"erro": "Todos os campos são obrigatórios"}, 400

        
        if categoria not in ['contas', 'lazer', 'estudos', 'streaming', 'delivery', 'supermercado', 'shopping']:
            return {"erro": "Categoria inválida"}, 400

        
        return insert_expense(id_user, nome, data_gasto, valor, categoria)
    except Exception as e:
        return {"erro": f"Erro ao criar o gasto: {str(e)}"}, 500

def get_total_expenses_service(id_user):
   
    try:
        df = get_expenses_data(id_user)

       
        if df is None or df.empty:
            return {"erro": "Nenhum gasto encontrado."}, 404

        total = df['valor'].sum()

        return {
            "total_gastos": float(total)
        }
    except Exception as e:
        return {"erro": f"Erro ao calcular o total de gastos: {str(e)}"}, 500

def get_highest_expense_service(id_user):
    try:
        print(f"[INFO] Buscando o maior gasto para o id_user: {id_user}")
        
       
        result = get_highest_expense(id_user)

       
        if isinstance(result, dict) and "erro" in result:
            print(f"[INFO] Erro ao buscar maior gasto: {result}")
            return result, 404  

       
        result_dict = {
            "id": int(result['id']),  
            "id_user": int(result['id_user']),  
            "nome": result['nome'],
            "data": str(result['data']),
            "valor": float(result['valor']),
            "categoria": result['categoria']
        }

        print(f"[INFO] Maior gasto encontrado: {result_dict}")
        return result_dict, 200  
    except Exception as e:
        print(f"[ERRO] Falha ao buscar maior gasto: {str(e)}")
        return {"erro": f"Erro ao buscar o maior gasto: {str(e)}"}, 500


def get_category_with_highest_expense_service(id_user):
 
    df, status_code = get_expenses_data(id_user)

    if df is None or df.empty:
        return {"erro": "Nenhum gasto encontrado."}, 404 

   
    categoria_totais = df.groupby('categoria')['valor'].sum()

   
    categoria_maior_gasto = categoria_totais.idxmax()
    valor_maior_gasto = categoria_totais.max()

    return {  
        "categoria_com_maior_gasto": {
            "categoria": categoria_maior_gasto,
            "valor": float(valor_maior_gasto)
        }
    }, 200 

def get_expenses_count_by_category_service(id_user):
   
    try:
        result = get_expenses_count_by_category(id_user)

       
        if isinstance(result, tuple) and result[1] == 404:
            return result  

        return result
    except Exception as e:
        return {"erro": f"Erro ao buscar contagem de gastos por categoria: {str(e)}"}, 500

def get_category_with_lowest_expense_service(id_user):
    
    try:
        result = get_category_with_lowest_expense(id_user)

       
        if isinstance(result, tuple) and result[1] == 404:
            return result  

        return result
    except Exception as e:
        return {"erro": f"Erro ao buscar a categoria com menor gasto: {str(e)}"}, 500

def get_user_expenses_service():
    try:
        print("[INFO] Requisição para obter os gastos do usuário.")
        
       
        result, status = get_user_expenses(request.args.get('id_user'))
        
        print(f"[INFO] Resultado das buscas: {result}, Status: {status}")
        
       
        return jsonify(result), status

    except Exception as e:
        print(f"[ERRO] Falha ao buscar os gastos do usuário: {e}")
      
        return jsonify({"erro": "Erro interno no servidor."}), 500