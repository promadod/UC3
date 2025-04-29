"""Readme Jogo da forca 2.0 feito por Iago Michael.
Alterações feitas da versão 1.0 Douglas Kleem
1º mudança de lista para comando requests
2º aumento de numero de tentativas
3º aumento de dificuldade das palvras
4º tratamento e redundancia caso falhar a lista por url acessar uma lista diferete """



import random
import requests # Biblioteca para fazer requisições HTTP, usada para baixar as palavras do link que você forneceu.

def obter_palavras(url):
    try: # comando try except para tratar se caso o link com as palavras der ruim usar a lista do return 
        resposta = requests.get(url) # Faz a requisição HTTP para obter o conteúdo do link
        resposta.raise_for_status() # Verifica se houve erro na requisição (Exemplo: erro 404)
        palavras = resposta.text.splitlines()  # Divide as palavras por linha
        return palavras
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar palavras: {e}")
        return ["python", "programacao", "computador", "algoritmo", "desenvolvimento","biblioteca","script","sistemas"] # Lista alternativa caso haja erro

def jogo_da_forca(url):
    palavras_reais = obter_palavras(url)  # Obtém palavras a partir do link
    palavra_secreta = random.choice(palavras_reais)  # Escolhe uma palavra válida aleatória
    letras_corretas = set()
    tentativas = 8
    
    while tentativas > 0:
        # Mostra a palavra com letras adivinhadas
        palavra_exibida = "".join(letra if letra in letras_corretas else "_" for letra in palavra_secreta)
        print(palavra_exibida)

        if palavra_exibida == palavra_secreta:
            print("Parabéns! Você venceu!")
            return
        
        # Pede uma letra
        letra = input("Digite uma letra: ").lower()
        
        if letra in letras_corretas:
            print("Você já tentou essa letra.")
        elif letra in palavra_secreta:
            letras_corretas.add(letra)
            print("Letra correta!")
        else:
            tentativas -= 1
            print(f"Letra incorreta! Tentativas restantes: {tentativas}")
    
    print(f"Game over! A palavra era: {palavra_secreta}")

# Substitua pelo link que você encontrou
url_palavras = "https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt"  
jogo_da_forca(url_palavras)
