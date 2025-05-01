#Cada numeração corresponde a um programa diferente para que seja desenvolvido. As atividades seguem abaixo:

#1.Filtre produtos com preço > 1000 usando list comprehension;

# Lista de produtos com preços
produtos = [
    {"nome": "Notebook", "preco": 3500},
    {"nome": "Smartphone", "preco": 1200},
    {"nome": "Fone de Ouvido", "preco": 200},
    {"nome": "Monitor", "preco": 800},
    {"nome": "Cadeira Gamer", "preco": 1500}
]

# Variavel para armazenar produtos com preço maior que 1000
produtos_filtrados = [produto for produto in produtos if produto["preco"] > 1000]

# Exibi a lista de e os produtos filtrados
print(f'Produtos com preço maior que 1000: {produtos_filtrados}')


#2.Conte quantos produtos existem por categoria (usar dicionário);


produtos = {
    "Eletrônicos": [
        {"nome": "Notebook", "preco": 3500},
        {"nome": "Smartphone", "preco": 1200},
        {"nome": "Monitor", "preco": 800}
    ],
    "Acessórios": [
        {"nome": "Fone de Ouvido", "preco": 200},
        {"nome": "Teclado Mecânico", "preco": 400},
        {"nome": "Mouse", "preco": 150}
    ],
    "Móveis": [
        {"nome": "Cadeira Gamer", "preco": 1500},
        {"nome": "Mesa para Computador", "preco": 900}
    ]
}

# Criando dicionário para armazenar contagem por categoria
contagem_categorias = {}

# Exibindo os produtos por categoria
for categoria, itens in produtos.items():
    print(f"\nCategoria: {categoria}")
    
    # Contagem de produtos por categoria
    contagem_categorias[categoria] = len(itens)
    
    for item in itens:
        print(f"- {item['nome']} | Preço: R$ {item['preco']}")

# Exibindo a quantidade total de produtos por categoria
print("\nQuantidade de produtos por categoria:")
for categoria, quantidade in contagem_categorias.items():
    print(f"{categoria}: {quantidade} produto(s)")



#3.Remova duplicatas de uma lista de pedidos usando set.

# Lista de pedidos com itens duplicados
pedidos = ["Notebook", "Smartphone", "Monitor", "Notebook", "Teclado", "Smartphone", "Mouse"]

# Removendo duplicatas usando set
pedidos_unicos = list(set(pedidos))

# Exibindo a lista sem duplicatas
print(pedidos_unicos)




#4.Uma empresa contratou seus serviços para armazenar dados de colaboradores em memória e realizar operações como:
'''
Adicionar novos colaboradores.
Buscar colaborador por ID.
Listar colaboradores com salário acima de X.
'''
#Implemente utilizando funções.

# Lista para armazenar colaboradores
colaboradores = []

# Função para adicionar um novo colaborador
def adicionar_colaborador(id, nome, cargo, salario):
    colaboradores.append({"id": id, "nome": nome, "cargo": cargo, "salario": salario})
    print(f"Colaborador {nome} adicionado com sucesso!")

# Função para buscar colaborador por ID
def buscar_colaborador(id):
    for colaborador in colaboradores:
        if colaborador["id"] == id:
            return colaborador
    return "Colaborador não encontrado."

# Função para listar colaboradores com salário acima de X
def listar_colaboradores_por_salario(minimo):
    return [colaborador for colaborador in colaboradores if colaborador["salario"] > minimo]

# Testando as funções
adicionar_colaborador(1, "Carlos Silva", "Desenvolvedor", 4500)
adicionar_colaborador(2, "Ana Souza", "Gerente", 7000)
adicionar_colaborador(3, "João Oliveira", "Analista", 3000)

print("\nBusca por ID:")
print(buscar_colaborador(2))  # Retorna os dados de Ana Souza

print("\nColaboradores com salário acima de 4000:")
print(listar_colaboradores_por_salario(4000))  # Lista apenas quem ganha mais que 4000
