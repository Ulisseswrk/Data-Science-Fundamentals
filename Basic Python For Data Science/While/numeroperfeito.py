while True:
    num = int(input("Digite um número: "))
    if num == 0:
        break

    soma = 0
    contador = 1

    while contador != num:
        if num % contador == 0:
            soma += contador
        contador += 1

    if soma == num:
        print("O número é perfeito")
    else:
        print("O número não é perfeito")
        break