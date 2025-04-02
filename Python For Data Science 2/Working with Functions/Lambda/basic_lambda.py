#código extremamente simples mas contém duas funções que eu não costumava usar

frase = input("Digite uma frase: ")
frase = frase.replace("."," ").replace(";"," ").replace("^"," ").split()

selecao = filter(lambda x: len(x) >= 5, frase)

for i in selecao:
    print("As palavras que possuem cinco ou mais letras foram: ")
    print(i)