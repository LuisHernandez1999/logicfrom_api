##### aqui uso as funçoes pra interagir com a classe 

from classes import User

def criar_user():
    nome = input('Entre seu nome: ')
    sobrenome = input('Entre seu sobrenome: ')
    email = input('Entre seu email: ')
    senha = input('Entre sua senha: ')
    
    confirmacao_senha = input('Confirme sua senha: ')
    while confirmacao_senha != senha:
        print("Senhas não são iguais. Por favor, tente novamente.")
        confirmacao_senha = input('Confirme sua senha: ')
    
    print(f"Usuário criado com sucesso!\nNome: {nome} {sobrenome}\nEmail: {email}")
    
   ##### a classe user 
    return User(nome, sobrenome, email, senha)

def login():
    email_cadastrado = input("entre seu email")
    senha_confirmacao = input("entre sua senha ")      
    
    email = input('Entre seu email: ')
    while email != email_cadastrado:
        print("Email incorreto. Tente novamente.")
        email = input('Entre seu email: ')
    print("Email confere.")

    senha = input('Entre sua senha: ')
    while senha != senha_confirmacao:
        print("Senha incorreta. Tente novamente.")
        senha = input('Entre sua senha: ')
    print("Login realizado com sucesso!")

    

    
