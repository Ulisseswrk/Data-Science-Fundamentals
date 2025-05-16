nome = input("Digite o nome do cliente para validação: ")
x = True
contador = 1

for i in nome:
    if contador == 1 and nome[0].islower():
        print("A primeira tem que ser maiuscula ")
        contador += 1
        x = False

    if i.isdigit():
        print("Não pode conter números")
        x = False
        break
    elif x:
        print("Tudo certo!")
        break