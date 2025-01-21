###### aqui defino a classe que as funçoes irá trabalhar 

class User:
    def __init__(self, nome, sobrenome, email, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.senha = senha

    def verificar_email(self, confirmacao_email):
        if confirmacao_email != self.email:
            print('Os emails não são iguais. Por favor, tente novamente.')
            return False
        else:
            print('Email confirmado:', confirmacao_email)
            return True

    def verificar_senha(self, confirmacao_senha):
        if confirmacao_senha != self.senha:
            print('As senhas não são iguais. Por favor, tente novamente.')
            return False
        else:
            print('Senha confirmada:', confirmacao_senha)
            return True


