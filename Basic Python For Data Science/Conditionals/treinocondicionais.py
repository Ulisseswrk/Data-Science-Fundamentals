numeros = []
for i in range(2):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)
    
while True:
    funcao = int(input("\nDigite 1 para par e impar:\nDigite 2 para positivo ou negativo:\nDigite 3 para inteiro ou decimal: "))

    if funcao < 1 or funcao > 3:
        print("Digite um número válido e tente novamente")
        continue

    else:
        break

if funcao == 1:
    if numeros[0] % 2 == 0 and numeros[1] % 2 != 0:
        print("O primeiro número é par e o segundo impar")
    
    elif numeros[0] % 2 != 0 and numeros[1] % 2 == 0:
        print("O primeiro número é impar e o segundo par")

    elif numeros[0] % 2 == 0 and numeros[1] % 2 == 0:
        print("Ambos os números são par")

    else:
        print("Ambos os números são impar")

elif funcao == 2:
    if numeros[0] >= 1 and numeros[1] < 1:
        print("O primeiro número é positivo e o segundo negativo")
    
    elif numeros[0] < 1 and numeros[1] >= 1:
        print("O primeiro número é negativo e o segundo positivo")

    elif numeros[0] >= 1 and numeros[1] >= 1:
        print("Ambos os números são positivos")

    elif 1 > numeros[0] != 0 and 1 > numeros[1] != 0:
        print("Ambos os números são negativos")
    
    elif numeros[0] == 0 and numeros[1] < 1:
        print("O primeiro número é neutro e o segundo negativo")

    elif numeros[0] == 0 and numeros[1] >= 1:
        print("O primeiro número é neutro e o segundo positivo")

    elif numeros[0] < 1 and numeros[1] == 0:
        print("O primeiro número é negativo e o segundo neutro")

    elif numeros[0] >= 1 and numeros[1] == 0:
        print("O primeiro número é positivo e o segundo neutro")

    else:
        print("Ambos os números são neutros")

elif funcao == 3:
    if numeros[0] % 1 == 0 and 0 < (numeros[1] % 1) > 0:
        print("O primeiro número é inteiro e o segundo decimal")

    elif 0 < (numeros[0] % 1) > 0 and numeros[1] % 1 == 0:
        print("O primeiro número é decimal e o segundo inteiro")

    elif 0 < (numeros[0] % 1) > 0 and 0 < (numeros[1] % 1) > 0:
        print("Ambos os números são decimais")
    
    elif numeros[0] % 1 == 0 and numeros[1] % 1 == 0:
        print("Ambos os números são inteiros")

