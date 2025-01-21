##### um exemplo de como usar essas funçoes 


from funcao import criar_user, login

def main():
    print("Bem-vindo ao sistema de gestão de usuários!")
    print("1. Criar Usuário")
    print("2. Login")
    print("3. Sair")
    
    while True:
        opcao = input("\nEscolha uma opção: ")
        if opcao == "1":
            print("\n=== Criar Usuário ===")
            user = criar_user()  
            print(f"\nUsuário criado com sucesso! Bem-vindo, {user.nome}!")
        
        elif opcao == "2":
            print("\n=== Login ===")
            login()
        
        elif opcao == "3":
            print("\nSaindo do sistema. Até logo!")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
