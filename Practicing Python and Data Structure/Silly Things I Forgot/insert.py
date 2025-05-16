lista = ['Ana', 'Pedro', 'Carlos']
contador = 1

nome = input('Digite o nome do novo convidado: ').capitalize()
posicao = int(input('Digite a sua posição: '))

lista.insert(posicao + 1,nome)
print(lista)