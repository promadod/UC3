# Crie um programa que:
'''
Armazene usuários (nome, e-mail) em um arquivo.
Liste todos os usuários.
Permita excluir um usuário.
'''
import os

# Nome do arquivo onde os dados serão armazenados
ARQUIVO_USUARIOS = "usuarios.txt"

# Função para gerar 20 usuários automaticamente e salvar no arquivo
def gerar_usuarios():
    '''Cria usuarios e e-mail aleatoriamente usando range'''
    nomes = [f"Usuario{i}" for i in range(1, 21)]
    emails = [f"usuario{i}@ig.com.br" for i in range(1, 21)]

    with open(ARQUIVO_USUARIOS, "w") as arquivo:
        i = 0
        while i < 20:
            arquivo.write(f"{nomes[i]},{emails[i]}\n")
            i += 1
    print("20 usuários foram gerados e armazenados com sucesso!")

# Função para listar todos os usuários do arquivo
def listar_usuarios():
    if not os.path.exists(ARQUIVO_USUARIOS):
        print("Nenhum usuário cadastrado ainda.")
        return

    with open(ARQUIVO_USUARIOS, "r") as arquivo:
        usuarios = arquivo.readlines()

    if usuarios:
        print("\nLista de Usuários:")
        for usuario in usuarios:
            nome, email = usuario.strip().split(",")
            print(f"Nome: {nome} | E-mail: {email}")
    else:
        print("Nenhum usuário cadastrado ainda.")

# Função para excluir um usuário pelo nome
def excluir_usuario(nome_excluir):
    if not os.path.exists(ARQUIVO_USUARIOS):
        print("Nenhum usuário cadastrado para excluir.")
        return

    with open(ARQUIVO_USUARIOS, "r") as arquivo:
        usuarios = arquivo.readlines()

    usuarios_filtrados = [usuario for usuario in usuarios if not usuario.startswith(nome_excluir + ",")]

    if len(usuarios_filtrados) == len(usuarios):
        print(f"Usuário {nome_excluir} não encontrado.")
    else:
        with open(ARQUIVO_USUARIOS, "w") as arquivo:
            arquivo.writelines(usuarios_filtrados)
        print(f"Usuário {nome_excluir} foi removido com sucesso!")

# Gerando usuários automaticamente como no enunciado
gerar_usuarios()

# Menu para selecionar as opções de cima 
while True:
    print("\n1 - Listar Usuários\n2 - Excluir Usuário\n3 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        listar_usuarios()
    elif opcao == "2":
        nome_excluir = input("Digite o nome do usuário a ser removido: ")
        excluir_usuario(nome_excluir)
    elif opcao == "3":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida! Tente novamente.")
