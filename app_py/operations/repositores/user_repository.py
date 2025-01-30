# repositories/user_repository.py
import psycopg2
from datetime import datetime

# Função para validar o login de um usuário
def validar_user(email, senha):
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
        return user_data is not None
    except Exception as e:
        print(f"Erro ao validar usuário: {e}")
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

# Função para obter os dados do usuário pelo email
def get_user_data(email):
    try:
        conexao = psycopg2.connect(
            host="localhost",
            database="moneycontroltwo",
            user="postgres",
            password="luis27"
        )
        cursor = conexao.cursor()
        cursor.execute('''SELECT * FROM users WHERE email = %s''', (email,))
        user_data = cursor.fetchone()
        
        if user_data:
            return {
                "id": user_data[0],
                "nome": user_data[1],
                "sobrenome": user_data[2],
                "email": user_data[3]
            }
        else:
            return None  # Retorna None se não encontrar o usuário
    except Exception as e:
        print(f"Erro ao buscar dados do usuário: {e}")
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

# Função para inserir um usuário no banco de dados
def insert_user_into_db(nome, sobrenome, email, senha):
    try:
        conexao = psycopg2.connect(
            host="localhost",
            database="moneycontroltwo",
            user="postgres",
            password="luis27"
        )
        cursor = conexao.cursor()

        # Insere os dados do usuário na tabela 'users'
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