#Enunciado: A partir da coluna com a informação dos Estados, crie um dicionário usando dict comprehension com a chave sendo o nome de um Estado e o valor sendo a contagem de vezes em que o Estado aparece na lista.


estados_repetidos = ['SP', 'ES', 'MG', 'MG', 'SP', 'MG', 'ES', 'ES', 'ES', 'SP', 'SP', 'MG', 'ES', 'SP', 'RJ', 'MG', 'RJ', 'SP', 'MG', 'SP', 'ES', 'SP', 'MG']

estados_unicos = list(set(estados_repetidos))
lista_listas = []

for estado in estados_unicos:
    lista = [i for i in estados_repetidos if i == estado]
    lista_listas.append(lista)

dicionario_estados = {estados_unicos[i]:len(lista_listas[i]) for i in range(len(estados_unicos))}

print(dicionario_estados)