lista = ['Ana', 'João', 'Pedro']

incorreto = input('Digite o nome incorreto: ').capitalize()
correto = input('Digite o nome correto: ').capitalize()

posicao = lista.index(incorreto)
lista.pop(posicao) # ou então o remove 
lista.insert(posicao, correto)

print(lista)