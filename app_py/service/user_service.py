# services/user_service.py
from app_py.operations.repositores.user_repository import insert_user_into_db, get_user_data, validar_user
import jwt
from datetime import datetime, timedelta

SECRET_WORD_FOR_LOGIN = "sua_secret_word"  # Defina um valor para o segredo aqui

# Serviço para login do usuário
def login_user_service(data):
    email = data.get('email')
    senha = data.get('senha')
    
    # Valida o login
    if not validar_user(email, senha):
        raise Exception("Email ou senha incorretos.")
    
    user_data = get_user_data(email)
    
    # Criação do token JWT
    token_payload = {
        "nome": user_data['nome'],
        "email": user_data['email'],
        "exp": datetime.utcnow() + timedelta(hours=1)  # Token expira após 1 hora
    }
    token = jwt.encode(token_payload, SECRET_WORD_FOR_LOGIN, algorithm="HS256")
    
    # Retorna o token e os dados do usuário
    return token, user_data

# Serviço para criação de usuário
def create_user_service(data):
    nome = data.get('nome')
    sobrenome = data.get('sobrenome')
    email = data.get('email')
    senha = data.get('senha')
    
    # Validação simples: verifica se o email já existe
    if get_user_data(email):
        raise Exception("Email já cadastrado.")
    
    # Chama o repositório para inserir o novo usuário
    insert_user_into_db(nome, sobrenome, email, senha)
    
    # Recupera os dados do usuário recém-criado
    user_data = get_user_data(email)
    
    # Retorna os dados do usuário
    return user_data
