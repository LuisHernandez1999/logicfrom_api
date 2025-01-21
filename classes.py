class User:
    def __init__(self, nome, sobrenome, email, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.senha = senha

    def verificar_email(self, confirmacao_email):
        return confirmacao_email == self.email

    def verificar_senha(self, confirmacao_senha):
        return confirmacao_senha == self.senha


