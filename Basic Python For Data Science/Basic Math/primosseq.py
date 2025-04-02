primos = []
num = int(input("Digite um número: "))

for numeros in range(2,num):
    eprimo = True

    for numero in range(2,numeros):
        if numeros % numero == 0:
            eprimo = False
            break

    if eprimo:
        primos.append(numeros)

print(f"Na sequencia de numeros até {num} estes são os primos:\t{primos}")