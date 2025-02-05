from app_py.operations.repositories.expense_repository import insert_expense

def create_expense(data):
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