desc = input("Digite a descrição da receita: ")

for i in desc:
    if i.isdigit():
        print("Esse é o código da receita: ",i, end="")