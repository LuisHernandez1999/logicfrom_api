import psycopg2
import pandas as pd
from database.db import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD

def insert_expense(id_user, nome, data, valor, categoria):
    """insere um gasto na tabela 'gastos'."""
    try:
        conexao = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = conexao.cursor()

        # consulta para inserir um novo gasto
        query = '''
            INSERT INTO gastos (id_user, nome, data, valor, categoria)
            VALUES (%s, %s, %s, %s, %s) RETURNING id;
        '''
        
        cursor.execute(query, (id_user, nome, data, valor, categoria))
        
        # recuperar o ID do gasto recém-inserido
        gasto_id = cursor.fetchone()[0]

        conexao.commit()
        
        print(f"gasto inserido com sucesso. ID: {gasto_id}")
        return {"mensagem": "Gasto inserido com sucesso.", "id": gasto_id}, 201

    except Exception as e:
        print(f"Erro ao inserir gasto: {e}")
        return {"erro": "Erro ao inserir gasto."}, 500

    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()


def get_expenses_data():
    """retorna todos os gastos registrados no banco """
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

        cursor.execute("SELECT * FROM gastos;")
        # cria um dataframe com todos os dados dos gastos
        colunas = [desc[0] for desc in cursor.description]
        df = pd.DataFrame(cursor.fetchall(), columns=colunas)

        return df

    except Exception as e:
        print(f"Erro ao buscar dados dos gastos: {e}")
        return None

    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()


def get_highest_expense():
    """retorna o gasto com o maior valor registrado usando Pandas."""
    df = get_expenses_data()

    if df is None or df.empty:
        return {"erro": "Nenhum gasto encontrado."}, 404

    highest_expense = df.loc[df['valor'].idxmax()]

    return {
        "id": highest_expense['id'],
        "id_user": highest_expense['id_user'],
        "nome": highest_expense['nome'],
        "data": str(highest_expense['data']),
        "valor": float(highest_expense['valor']),
        "categoria": highest_expense['categoria']
    }


def get_lowest_expense():
    """retorna o gasto com o menor valor registrado """
    df = get_expenses_data()

    if df is None or df.empty:
        return {"erro": "Nenhum gasto encontrado."}, 404

    lowest_expense = df.loc[df['valor'].idxmin()]

    return {
        "id": lowest_expense['id'],
        "id_user": lowest_expense['id_user'],
        "nome": lowest_expense['nome'],
        "data": str(lowest_expense['data']),
        "valor": float(lowest_expense['valor']),
        "categoria": lowest_expense['categoria']
    }
def get_category_with_highest_expense():
    """retorna a categoria com o maior gasto e seu valor."""
    df = get_expenses_data()

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
    }

def get_category_with_lowest_expense():
    """retorna a categoria com o menor gasto e seu valor."""
    df = get_expenses_data()

    if df is None or df.empty:
        return {"erro": "Nenhum gasto encontrado."}, 404

    # agrupar os dados por categoria e somar os valores de cada categoria
    categoria_totais = df.groupby('categoria')['valor'].sum()

    # encontrar a categoria com menor gasto
    categoria_menor_gasto = categoria_totais.idxmin()
    valor_menor_gasto = categoria_totais.min()

    return {
        "categoria_com_menor_gasto": {
            "categoria": categoria_menor_gasto,
            "valor": float(valor_menor_gasto)
        }
    }    
def get_expenses_count_by_category():
    """retorna a quantidade de gastos por categoria."""
    df = get_expenses_data()

    if df is None or df.empty:
        return {"erro": "Nenhum gasto encontrado."}, 404

    # contar o número de gastos por categoria
    categoria_contagem = df.groupby('categoria')['id'].count()

    return categoria_contagem.to_dict()  # retorna um dicionário com a contagem por categoria



def get_total_expenses():
    """Retorna o total de gastos registrados no banco de dados."""
    df = get_expenses_data()

    if df is None or df.empty:
        return {"erro": "Nenhum gasto encontrado."}, 404

    total_gastos = df['valor'].sum()  

    return {
        "total_gastos": float(total_gastos)
    }