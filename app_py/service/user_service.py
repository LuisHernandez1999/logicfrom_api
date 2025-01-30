# services/user_service.py
from app_py.operations.repositores.user_repository import insert_user_into_db, get_user_data, validar_user
import jwt
from datetime import datetime, timedelta

SECRET_WORD_FOR_LOGIN = "56646"  


def login_user_service(data):
    email = data.get('email')
    senha = data.get('senha')
    
    
    if not validar_user(email, senha):
        raise Exception("Email ou senha incorretos.")
    
    user_data = get_user_data(email)
    
    
    token_payload = {
        "nome": user_data['nome'],
        "email": user_data['email'],
        "exp": datetime.utcnow() + timedelta(hours=1)  
    }
    token = jwt.encode(token_payload, SECRET_WORD_FOR_LOGIN, algorithm="HS256")
    
  
    return token, user_data


def create_user_service(data):
    nome = data.get('nome')
    sobrenome = data.get('sobrenome')
    email = data.get('email')
    senha = data.get('senha')
    
   
    if get_user_data(email):
        raise Exception("Email já cadastrado.")
    

    insert_user_into_db(nome, sobrenome, email, senha)
    
  
    user_data = get_user_data(email)
    
   
    return user_data
