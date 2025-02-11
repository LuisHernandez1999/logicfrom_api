import psycopg2
import pandas as pd
from database.db import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD

def insert_expense(id_user, nome, data, valor, categoria):
   
    try:
        conexao = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = conexao.cursor()

      
        query = '''
            INSERT INTO gastos (id_user, nome, data, valor, categoria)
            VALUES (%s, %s, %s, %s, %s) RETURNING id;
        '''
        
        cursor.execute(query, (id_user, nome, data, valor, categoria))
        
       
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


def get_expenses_data(id_user):
   
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

       
        cursor.execute("SELECT * FROM gastos WHERE id_user = %s;", (id_user,))

      
        colunas = [desc[0] for desc in cursor.description]
        df = pd.DataFrame(cursor.fetchall(), columns=colunas)

        if df.empty:
            return None, 404  

      
        return df, 200

    except Exception as e:
        print(f"Erro ao obter os dados de gastos: {e}")
        return None, 500  

    finally:
      
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

def get_highest_expense(id_user):
   
    print(f"[INFO] Buscando o maior gasto no banco de dados para id_user: {id_user}")
    
    df, status_code = get_expenses_data(id_user)

    if df is None or df.empty:
        print(f"[INFO] Nenhum gasto encontrado para o id_user: {id_user}. Retornando erro.")
        return {"erro": "Nenhum gasto encontrado para o usuário."}, 404

    highest_expense = df.loc[df['valor'].idxmax()]

    print(f"[INFO] Maior gasto encontrado: {highest_expense}")
    
    return {
        "id": highest_expense['id'],
        "id_user": highest_expense['id_user'],
        "nome": highest_expense['nome'],
        "data": str(highest_expense['data']),
        "valor": float(highest_expense['valor']),
        "categoria": highest_expense['categoria']
    }

def get_lowest_expense(id_user):
    df, status_code = get_expenses_data(id_user)
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
def get_category_with_highest_expense(id_user):
  
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
    }

def get_category_with_lowest_expense(id_user):
    """retorna a categoria com o menor gasto e seu valor."""
    df, status_code = get_expenses_data(id_user)

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
def get_expenses_count_by_category(id_user):
    """retorna a quantidade de gastos por categoria."""
    df = get_expenses_data()

    if df is None or df.empty:
        return {"erro": "Nenhum gasto encontrado."}, 404

    # contar o número de gastos por categoria
    categoria_contagem = df.groupby('categoria')['id'].count()

    return categoria_contagem.to_dict()  # retorna um dicionário com a contagem por categoria



def get_total_expenses(id_user):
  
    df, status_code = get_expenses_data(id_user)

    if df is None or df.empty:
        return {"erro": "Nenhum gasto encontrado."}, 404

    total_gastos = df['valor'].sum()

    return {
        "total_gastos": float(total_gastos)
    }


def  get_user_expenses(id_user):
  
    df, status_code = get_expenses_data(id_user)

    if df is None or df.empty:
        return {"erro": "Nenhum gasto encontrado para o usuário."}, 404

   
    gastos = []
    for _, row in df.iterrows():
        gasto = {
            "nome": row.get('nome'),
            "data": str(row.get('data')),  
            "valor": float(row.get('valor')),
            "categoria": row.get('categoria')
        }
        gastos.append(gasto)

    return {
        "gastos": gastos
    }