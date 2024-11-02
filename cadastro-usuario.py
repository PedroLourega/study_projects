#Dicionario de usuarios
usuarios = {}

#Função para registrar usuário
def registrar_usuario(username, nome, email):
    if username in usuarios:
        print("Usuário {username} registrado com sucesso.")
    else:
        usuarios[username] = {"nome": nome, "email": email}
        print(f"Usuário {username} registrando com sucesso.")

# Função para atualizar dados do usuário
def atualizar_usuario(username, nome=None, email=None):
    if username in usuarios:
        if nome:
            usuarios[username]["nome"] = nome
        if email:
            usuarios[username]["email"] = email
        print(f"Dados de {username} atualizados com sucesso.")
    else:
        print("Usuário não encontrado.")

#Função para excluir um usuário
def excluir_usuario(username):
    if username in usuarios:
        del usuarios[username]
        print(f"Usuário {username} excluido com sucesso.")
    else:
        print("Nenhum usuário cadastro.")


#Listar os usuários
def listar_usuarios():
    if usuarios:
        print("Usuários cadastrados: ")
        for username, dados in usuarios.items():
            print(f"Username: {username}, Nome: {dados['nome']}, Email: {dados['email']}")
        else:
            print("Nenhum usuário cadastrado.")

def menu():
    while True:
        print("-------Menu de Cadastros de Usuário-------")
        print("1. Registrar novo usuário")
        print("2. Atualizar usuário")
        print("3. Excluir usuário")
        print("4. Listar usuário")
        print("5. Sair")
        print("------------------------------------------")


        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            username = input("Digite o username: ")
            nome =  input("Digite o nome completo: ")
            email = input("Digite o email: ")
            registrar_usuario(username, nome, email)
        elif opcao == "2":
            username = input("Digite o username do username do usuário a ser atualizado: ")
            nome = input("Digite o novo nome completo (ou pressione Enter para manter): ")
            atualizar_usuario(username, nome if nome else None, email if email else None)
        elif opcao == "3":
            username = input("Digite o username do usuário a ser excluido: ")
            excluir_usuario(username)
        elif opcao == "4":
            listar_usuarios()
        elif opcao == "5":
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida! Tente novamente.")

menu()

