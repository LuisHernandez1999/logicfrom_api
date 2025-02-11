# app_py/controllers/user_controller.py
from flask import request, jsonify
from app_py.service.user_service import login_user_service, create_user_service  
import jwt
SECRET_KEY = 'chave1'
# controla o login do usuário
def login_user():
    data = request.get_json()
    try:
        token, user_data = login_user_service()
        
        # retorna a resposta com o token e os dados do usuário
        return jsonify({
            "message": f"Login realizado com sucesso! Bem-vindo(a), {user_data['nome']}!",
            "usuario": user_data,
            "token": token
        }), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


# controla a criação do usuário
def api_criar_user():
    data = request.get_json()
    try:
        user_data = create_user_service(data)
        return jsonify({
            "message": "Usuário criado com sucesso!",
            "usuario": user_data
        }), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 500
def get_user_from_token():
   
    token = request.headers.get('Authorization')

    if not token:
        return None  

    if token.startswith('Bearer '):
        token = token[7:]  

    try:
      
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        
       
        id_user = decoded_token.get('id_user')
        
        if id_user:
            return id_user  
        else:
            return None 
    except jwt.ExpiredSignatureError:
        return None  
    except jwt.InvalidTokenError:
        return None  