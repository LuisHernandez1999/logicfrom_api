from app_py.operations.repositories.expense_repository import insert_expense, get_expenses_count_by_category, get_highest_expense, get_expenses_data, get_category_with_highest_expense, get_category_with_lowest_expense

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

def get_total_expenses_service():
   
    try:
        df = get_expenses_data()

       
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


def get_category_with_highest_expense_service():
   
    try:
        result = get_category_with_highest_expense()

        
        if isinstance(result, tuple) and result[1] == 404:
            return result  

        
        return result
    except Exception as e:
        return {"erro": f"Erro ao buscar a categoria com maior gasto: {str(e)}"}, 500

def get_expenses_count_by_category_service():
   
    try:
        result = get_expenses_count_by_category()

       
        if isinstance(result, tuple) and result[1] == 404:
            return result  

        return result
    except Exception as e:
        return {"erro": f"Erro ao buscar contagem de gastos por categoria: {str(e)}"}, 500

def get_category_with_lowest_expense_service():
    
    try:
        result = get_category_with_lowest_expense()

       
        if isinstance(result, tuple) and result[1] == 404:
            return result  

        return result
    except Exception as e:
        return {"erro": f"Erro ao buscar a categoria com menor gasto: {str(e)}"}, 500
