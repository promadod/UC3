# Atividade Prática: Sistema de uma Biblioteca
'''
Contexto:
Você foi contratado para desenvolver um sistema de gerenciamento de biblioteca usando POO em Python.
O sistema deve modelar livros, usuários e empréstimos, com funcionalidades básicas de cadastro, consulta e operações.

Requisitos:
- O sistema deve permitir o cadastro de livros, usuários e empréstimos.
- O sistema deve permitir a consulta de livros cadastrados.
- O sistema deve permitir a consulta de usuários cadastrados.
'''

# DESAFIO (opcional) Classe LivroDigital:
# Herde de Livro e adicione o formato do e-book e formas de download.

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas  # Biblioteca para criar PDFs

class Livro:
    def __init__(self, titulo, autor, ano, conteudo):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True  # Define se o livro está disponível para empréstimo
        self.conteudo = conteudo  # Guarda um conteúdo fictício para o livro

    def __str__(self):
        return f"{self.titulo} ({self.ano}) - {self.autor} - {'Disponível' if self.disponivel else 'Emprestado'}"

    def obter_informacoes(self):  
        linhas = len(self.conteudo.split('\n'))  # Conta o número de linhas no conteúdo do livro
        return f"Título: {self.titulo}\nAutor: {self.autor}\nAno: {self.ano}\nTotal de linhas: {linhas}"

    def transformar_em_ebook(self):  
        nome_pdf = f"{self.titulo.replace(' ', '_')}.pdf"  # Define o nome do arquivo PDF
        c = canvas.Canvas(nome_pdf, pagesize=A4)  # Cria um arquivo PDF com tamanho de página A4
        c.setFont("Helvetica", 12)  # Define a fonte e tamanho do texto no PDF
        c.drawString(100, 800, f"Ebook: {self.titulo}")  # Insere o título no PDF
        c.drawString(100, 780, f"Autor: {self.autor}")  
        c.drawString(100, 760, f"Ano: {self.ano}")  
        c.drawString(100, 740, f"Total de linhas: {len(self.conteudo.split('\n'))}")  

        y_position = 720  
        for linha in self.conteudo.split('\n'):  # Percorre cada linha do conteúdo do livro
            if y_position < 50:  # Se atingir o limite da página, cria uma nova
                c.showPage()  
                c.setFont("Helvetica", 12)  
                y_position = 800  
            c.drawString(100, y_position, linha)  # Adiciona a linha ao PDF
            y_position -= 20  

        c.save()  # Salva o arquivo PDF
        print(f"Ebook '{nome_pdf}' gerado com sucesso! ")  

class Usuario:
    def __init__(self, nome, id_usuario):
        self.nome = nome
        self.id_usuario = id_usuario

    def __str__(self):
        return f"Usuário: {self.nome}, ID: {self.id_usuario}"

class Biblioteca:
    def __init__(self):  
        self.livros = [
            Livro("Cavaleiros do Zodíaco", "Autor desconhecido", 1986, "Conteúdo fictício...\nLinha 2...\nLinha 3..."),
            Livro("Dragonball Z",          "Akira Toriyama", 1989, "Goku e Vegeta lutam...\nLinha 2...\nLinha 3..."),
            Livro("Liga da Justiça",       "DC Comics", 1960, "Superman, Batman e Mulher-Maravilha...\nLinha 2...\nLinha 3..."),
            Livro("Caverna do Dragão", "Mark Evanier", 1983, "O grupo tenta voltar para casa...\nLinha 2...\nLinha 3...")
        ]
        self.usuarios = [
            Usuario("Iago Michael", 101),
            Usuario("Douglas Kleem", 102)
        ]
        self.emprestimos = {}  

    def cadastrar_livro(self):
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        ano = input("Digite o ano de publicação: ")
        conteudo = input("Digite uma prévia do conteúdo do livro: ")  
        livro = Livro(titulo, autor, ano, conteudo)
        self.livros.append(livro)
        print(f"Livro '{titulo}' cadastrado com sucesso!\n")

    def cadastrar_usuario(self):
        nome = input("Digite o nome do usuário: ")
        id_usuario = input("Digite o ID do usuário: ")
        usuario = Usuario(nome, id_usuario)
        self.usuarios.append(usuario)
        print(f"Usuário '{nome}' cadastrado com sucesso!\n")

    def consultar_livros(self):
        print("\n Livros disponíveis na biblioteca:")
        for livro in self.livros:
            print(livro)

    def consultar_usuarios(self):
        print("\n Usuários cadastrados:")
        for usuario in self.usuarios:
            print(usuario)

    def emprestar_livro(self):  
        titulo = input("Digite o título do livro que deseja emprestar: ")  
        id_usuario = input("Digite o ID do usuário que está pegando emprestado: ")  
        for livro in self.livros:  
            if livro.titulo == titulo and livro.disponivel:  
                livro.disponivel = False  
                self.emprestimos[titulo] = id_usuario  
                print(f"Livro '{titulo}' emprestado para ID {id_usuario}.\n")  
                return  
        print(f"O livro '{titulo}' não está disponível ou não existe.\n")  

    def devolver_livro(self):  
        titulo = input("Digite o título do livro que deseja devolver: ")  
        if titulo in self.emprestimos:  
            for livro in self.livros:  
                if livro.titulo == titulo:  
                    livro.disponivel = True  
                    del self.emprestimos[titulo]  
                    print(f"Livro '{titulo}' devolvido com sucesso!\n")  
                    return  
        print(f"O livro '{titulo}' não foi emprestado ou não existe.\n")  

    def gerar_ebook(self):  
        titulo = input("Digite o título do livro para transformar em Ebook: ")  
        for livro in self.livros:  
            if livro.titulo == titulo:  
                livro.transformar_em_ebook()  
                return  
        print(f"O livro '{titulo}' não foi encontrado.")  

biblioteca = Biblioteca()

while True:
    print("\n Sistema de Biblioteca")
    print("1 - Cadastrar Livro")
    print("2 - Cadastrar Usuário")
    print("3 - Consultar Livros")
    print("4 - Consultar Usuários")
    print("5 - Emprestar Livro")
    print("6 - Devolver Livro")
    print("7 - Transformar Livro em Ebook")
    print("8 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        biblioteca.cadastrar_livro()
    elif opcao == "2":
        biblioteca.cadastrar_usuario()
    elif opcao == "3":
        biblioteca.consultar_livros()
    elif opcao == "4":
        biblioteca.consultar_usuarios()
    elif opcao == "5":
        biblioteca.emprestar_livro()
    elif opcao == "6":
        biblioteca.devolver_livro()
    elif opcao == "7":
        biblioteca.gerar_ebook()
    elif opcao == "8":
        print("Saindo do sistema. Até mais!")
        break
    else:
        print("Opção inválida, tente novamente.\n")
