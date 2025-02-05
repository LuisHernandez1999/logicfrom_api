import psycopg2
from database.db import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD


def create_expense_na_tabela_gastos(id_user, nome, valor, data, categoria):

    conexao = None
    cursor = None
    try:
      
        conexao = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            client_encoding='UTF8'
        )
        cursor = conexao.cursor()

      
        query = '''
            INSERT INTO gastos (id_user, nome, valor, data, categoria)
            VALUES (%s, %s, %s, %s, %s) RETURNING id
        '''
        cursor.execute(query, (id_user, nome, valor, data, categoria))
        conexao.commit()

        gasto_id = cursor.fetchone()[0]  # pegar o ID do gasto recém-criado
        return {"mensagem": "Gasto criado com sucesso!", "id": gasto_id}, 201

    except Exception as e:
        return {"erro": f"Erro ao inserir gasto: {e}"}, 500

    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()