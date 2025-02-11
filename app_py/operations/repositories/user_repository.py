# repositories/user_repository.py
import psycopg2
from datetime import datetime

def validar_user(email, senha):
    cursor = None
    conexao = None
    try:
        conexao = psycopg2.connect(
            host="localhost",
            database="moneycontroltwo",
            user="postgres",
            password="luis27"
        )
        cursor = conexao.cursor()
        
       
        cursor.execute('''SELECT * FROM users WHERE email = %s AND senha = %s''', (email, senha))
        user_data = cursor.fetchone()
        
        # retorna True se os dados do usuário foram encontrados caso contrário False
        return user_data is not None
    
    except Exception as e:
       
        print(f"Erro ao validar usuário: {e}")
        return False 
    
    finally:
      
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()


def get_user_data(email):
    cursor = None
    conexao = None
    try:
        conexao = psycopg2.connect(
            host="localhost",
            database="moneycontroltwo",
            user="postgres",
            password="luis27"
        )
        cursor = conexao.cursor()
        
        # consulta SQL
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user_data = cursor.fetchone()
        
     
        if not user_data:
            raise Exception(f"Usuário com o email '{email}' não encontrado.")
        
       
        user_dict = {
            "id": user_data[0],         # id
            "nome": user_data[1],       # nome 
            "sobrenome": user_data[2],  # sobrenome 
            "email": user_data[3]       # email 
        }
        
        return user_dict
    
    except Exception as e:
       
        print(f"Erro ao buscar dados do usuário: {e}")
        raise 
    finally:
      
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

def insert_user_into_db(nome, sobrenome, email, senha):
    try:
        conexao = psycopg2.connect(
            host="localhost",
            database="moneycontroltwo",
            user="postgres",
            password="luis27"
        )
        cursor = conexao.cursor()

       
        cursor.execute('''
            INSERT INTO users (nome, sobrenome, email, senha)
            VALUES (%s, %s, %s, %s)
        ''', (nome, sobrenome, email, senha))

        conexao.commit()
    except Exception as e:
        print(f"Erro ao inserir usuário: {e}")
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()
