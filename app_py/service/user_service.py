# services/user_service.py
from app_py.operations.repositories.user_repository import insert_user_into_db, get_user_data, validar_user
import jwt
from datetime import datetime, timedelta


SECRET_WORD_FOR_LOGIN = "56646"  

def login_user_service(data):
    try:
       
        email = data.get('email')
        senha = data.get('senha')
        
        
        if not email or not senha:
            raise Exception("Email e senha são obrigatórios")
        
      
        if not validar_user(email, senha):
            raise Exception("Email ou senha incorretos.")
        
       
        user_data = get_user_data(email)
        
       
        print(f"[INFO] Tipo de user_data: {type(user_data)}")
        print(f"[INFO] Conteúdo de user_data: {user_data}")
        
       
        if not isinstance(user_data, dict):
            raise Exception(f"Erro: O tipo de 'user_data' não é um dicionário. Tipo recebido: {type(user_data)}")
        
      
        if 'nome' not in user_data or 'email' not in user_data:
            raise Exception("Erro: Dados do usuário não estão no formato esperado. 'nome' ou 'email' ausentes.")
        
        nome = user_data.get('nome')
        email_usuario = user_data.get('email')
        
        
        token_payload = {
            "nome": nome,
            "email": email_usuario,
            "exp": datetime.utcnow() + timedelta(hours=1)  
        }
        
      
        token = jwt.encode(token_payload, SECRET_WORD_FOR_LOGIN, algorithm="HS256")
        
        
        print(f"[INFO] Token gerado com sucesso: {token}")
        
        
        response_data = {
            "token": token
        }
        print(f"[INFO] Resposta JSON antes do retorno: {response_data}")
        
     
        return token, user_data 
    
    except Exception as e:
        
        print(f"[ERROR] Detalhes do erro: {e}")
        raise e  
    


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
