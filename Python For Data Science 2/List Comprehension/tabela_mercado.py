#Criacao de um sistema basico de mercados em que uma lista de tuplas é gerada

id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
quantidade = [15, 12, 1, 15, 2, 11, 2, 12, 2, 4]
preco = [93.0, 102.0, 18.0, 41.0, 122.0, 14.0, 71.0, 48.0, 14.0, 144.0]

lista_de_tuplas = ['IDs','Quantidade', 'Preco', 'Preco Total']
lista_de_tuplas += [(id[i], quantidade[i], preco[i], preco[i] * quantidade[i]) for i in range(len(id))]

print(lista_de_tuplas)