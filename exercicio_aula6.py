# Atividades Práticas:

# 1. Crie uma classe Conta com:
'''
Atributo _saldo (privado).
Getter saldo que retorna o valor formatado (ex: R$1000.00).
Setter que bloqueia valores negativos.
'''

class Conta:
    def __init__(self, saldo_inicial=0.0):
        self._saldo = max(saldo_inicial, 0.0)  # Garante que o saldo inicial não seja negativo 

    @property
    def saldo(self):
        return f"R${self._saldo:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            print("Erro: O saldo não pode ser negativo.")
        else:
            self._saldo = valor

# Testando a classe Conta de baco
conta = Conta(1500.75)
print(conta.saldo)  # Saída: R$1.500,75

conta.saldo = -200  # Tentativa de definir saldo negativo (erro esperado)
print(conta.saldo)  # Ainda R$1.500,75, pq a mudança não foi aceita

conta.saldo = 2500
print(conta.saldo)  # Saída: R$2.500,00


# 2. Classes Abstratas:
'''
Crie uma classe abstrata Animal com método comum a todas as classes-filhas.
Implemente, pelo menos, as classes Cachorro e Gato com 3 métodos para cada uma.
'''


from abc import ABC, abstractmethod

"""
 Classe abstrata Animal ...> Define emitir_som() como um método abstrato, forçando as classesfilhas a implementar.  
 Métodos get_raca() e get_cor() ==> Retornam a raça e cor do animal.  
 Classes Cachorro e Gato ---> Implementam o som específico de cada animal.  
 Criei objetos Cachorro e Gato e chamei os métodos para verificar o funcionamento."""

# Classe abstrata Animal
class Animal(ABC):
    def __init__(self, raca, cor):
        self.raca = raca
        self.cor = cor

    @abstractmethod
    def emitir_som(self):
        pass  # Método abstrato que será implementado nas classes-filhas

    def get_raca(self):
        return f"Raça: {self.raca}"

    def get_cor(self):
        return f"Cor: {self.cor}"

# Classe Cachorro (herda de Animal)
class Cachorro(Animal):
    def emitir_som(self):
        return "O cachorro faz: Au Au!"

# Classe Gato (herda de Animal)
class Gato(Animal):
    def emitir_som(self):
        return "O gato faz: Miau!"

# Testando as classes
cachorro = Cachorro("Labrador", "Dourado")
gato = Gato("Siamês", "Branco")

print(cachorro.emitir_som())  #  O cachorro faz: Au Au!
print(cachorro.get_raca())    #  Raça: Labrador
print(cachorro.get_cor())     # Cor: Dourado

print(gato.emitir_som())      # O gato faz: Miau!
print(gato.get_raca())        # Raça: Siamês
print(gato.get_cor())         # Cor: Branco


# 3. Padrão de Acesso a Repositórios

# Crie uma classe UsuarioRepository com os seguintes métodos:
'''
- cadastrar(usuario): cadastra um usuário (dicionário com nome e email).
- listar_todos(): retorna uma lista com todos os usuários cadastrados.
- buscar_por_email(email): retorna o usuário correspondente ao email informado.
- remover(email): remove o usuário correspondente ao email informado. 
- atualizar(usuario): atualiza os dados do usuário correspondente ao email informado.
- listar_por_nome(nome): retorna uma lista com todos os usuários que possuem o nome informado.
- listar_por_email(email): retorna uma lista com todos os usuários que possuem o email informado.
- listar_por_nome_e_email(nome, email): retorna uma lista com todos os usuários que possuem o nome e email informados.
'''

class UsuarioRepository:
    """ Armazena os usuários em uma lista (self.usuarios) como base de dados em memória.  
    Evita emails duplicados na função cadastrar, garantindo usuários unicos.  
    Lista todos os usuários cadastrados, permitindo verificações rápidas.  
    Busca, remove e atualiza usuários pelo email, garantindo operações seguras.  
    Listagens flexíveis  Busca por nome, email ou ambos, conforme solicitado pelo usuario."""
    def __init__(self):
        self.usuarios = []  # Lista de usuários armazenados em memória

    def cadastrar(self, usuario):
        """Cadastra um usuário (dicionário com nome e email)."""
        if any(u["email"] == usuario["email"] for u in self.usuarios):
            print(f"Erro: O email {usuario['email']} já está cadastrado.")
        else:
            self.usuarios.append(usuario)
            print(f"Usuário {usuario['nome']} cadastrado com sucesso!")

    def listar_todos(self):
        """Retorna a lista com todos os usuários cadastrados."""
        return self.usuarios

    def buscar_por_email(self, email):
        """Retorna o usuário correspondente ao email informado."""
        for usuario in self.usuarios:
            if usuario["email"] == email:
                return usuario
        return f"Usuário com email {email} não encontrado."

    def remover(self, email):
        """Remove o usuário correspondente ao email informado."""
        for usuario in self.usuarios:
            if usuario["email"] == email:
                self.usuarios.remove(usuario)
                return f"Usuário com email {email} removido com sucesso!"
        return f"Erro: Usuário com email {email} não encontrado."

    def atualizar(self, usuario):
        """Atualiza os dados do usuário correspondente ao email informado."""
        for i, u in enumerate(self.usuarios):
            if u["email"] == usuario["email"]:
                self.usuarios[i] = usuario
                return f"Usuário {usuario['nome']} atualizado com sucesso!"
        return f"Erro: Usuário com email {usuario['email']} não encontrado."

    def listar_por_nome(self, nome):
        """Retorna uma lista com todos os usuários que possuem o nome informado."""
        return [usuario for usuario in self.usuarios if usuario["nome"] == nome]

    def listar_por_email(self, email):
        """Retorna uma lista com todos os usuários que possuem o email informado."""
        return [usuario for usuario in self.usuarios if usuario["email"] == email]

    def listar_por_nome_e_email(self, nome, email):
        """Retorna uma lista com todos os usuários que possuem o nome e email informados."""
        return [usuario for usuario in self.usuarios if usuario["nome"] == nome and usuario["email"] == email]


#  Testando a classe
repo = UsuarioRepository()

# Cadastrando usuários
repo.cadastrar({"nome": "Andressa", "email": "andressa@ig.com.br"})
repo.cadastrar({"nome": "Douglas", "email": "douglas@ig.com.br"})
repo.cadastrar({"nome": "Alyfer", "email": "Alyfr@ig.com.br"})  # Testando email duplicado

# Listando todos os usuários
print("\nLista de usuários cadastrados:")
print(repo.listar_todos())

# Buscando usuário por email
print("\nBuscando usuário:")
print(repo.buscar_por_email("andressa@ig.com.br"))

# Removendo usuário
print("\nRemovendo usuário:")
print(repo.remover("douglas@ig.com.br"))
print(repo.listar_todos())

# Atualizando usuário
print("\nAtualizando usuário:")
repo.atualizar({"nome": "Andressa Motta", "email": "andressa@ig.com.br", "telefone": "98759-2136"})  # Adicionando telefone
print(repo.listar_todos())

# Listando por nome
print("\nListando usuários por nome:")
print(repo.listar_por_nome("Douglas"))

# Listando por nome e email
print("\nListando usuários por nome e email:")
print(repo.listar_por_nome_e_email("Douglas", "douglas@ig.com.br"))


# 4. DESAFIO: retorne às atividades 2 e 3 e implemente uma metaclasse dentro de seus respectivos contextos.

class UsuarioRepository:
    def __init__(self):
        self.usuarios = []  # Lista de usuários armazenados em memória

    def cadastrar(self, usuario):
        """Cadastra um usuário (dicionário com nome e email)."""
        if any(u["email"] == usuario["email"] for u in self.usuarios):
            print(f"Erro: O email {usuario['email']} já está cadastrado.")
        else:
            self.usuarios.append(usuario)
            print(f"Usuário {usuario['nome']} cadastrado com sucesso!")

    def listar_todos(self):
        """Retorna a lista com todos os usuários cadastrados."""
        return self.usuarios

    def buscar_por_email(self, email):
        """Retorna o usuário correspondente ao email informado."""
        for usuario in self.usuarios:
            if usuario["email"] == email:
                return usuario
        return f"Usuário com email {email} não encontrado."

    def remover(self, email):
        """Remove o usuário correspondente ao email informado."""
        for usuario in self.usuarios:
            if usuario["email"] == email:
                self.usuarios.remove(usuario)
                return f"Usuário com email {email} removido com sucesso!"
        return f"Erro: Usuário com email {email} não encontrado."

    def atualizar(self, usuario):
        """Atualiza os dados do usuário correspondente ao email informado."""
        for i, u in enumerate(self.usuarios):
            if u["email"] == usuario["email"]:
                self.usuarios[i] = usuario
                return f"Usuário {usuario['nome']} atualizado com sucesso!"
        return f"Erro: Usuário com email {usuario['email']} não encontrado."

    def listar_por_nome(self, nome):
        """Retorna uma lista com todos os usuários que possuem o nome informado."""
        return [usuario for usuario in self.usuarios if usuario["nome"] == nome]

    def listar_por_email(self, email):
        """Retorna uma lista com todos os usuários que possuem o email informado."""
        return [usuario for usuario in self.usuarios if usuario["email"] == email]

    def listar_por_nome_e_email(self, nome, email):
        """Retorna uma lista com todos os usuários que possuem o nome e email informados."""
        return [usuario for usuario in self.usuarios if usuario["nome"] == nome and usuario["email"] == email]


#  Testando a classe
repo = UsuarioRepository()

# Cadastrando usuários
repo.cadastrar({"nome": "Andressa", "email": "andressa@ig.com.br"})
repo.cadastrar({"nome": "Douglas", "email": "douglas@ig.com.br"})
repo.cadastrar({"nome": "Ana Menezes", "email": "ana@email.com"})  # Testando email duplicado

# Listando todos os usuários
print("\nLista de usuários cadastrados:")
print(repo.listar_todos())

# Buscando usuário por email
print("\nBuscando usuário:")
print(repo.buscar_por_email("douglas@ig.com.br"))

# Removendo usuário
print("\nRemovendo usuário:")
print(repo.remover("andressa@ig.com.br"))
print(repo.listar_todos())

# Atualizando usuário
print("\nAtualizando usuário:")
repo.atualizar({"nome": "Douglas Klem", "email": "douglas@ig.com.br", "telefone": "98748-1054"})  # Adicionando telefone
print(repo.listar_todos())

# Listando por nome
print("\nListando usuários por nome:")
print(repo.listar_por_nome("Eduardo Luparele"))

# Listando por nome e email
print("\nListando usuários por nome e email:")
print(repo.listar_por_nome_e_email("Douglas Klem", "douglas@ig.com.br"))
