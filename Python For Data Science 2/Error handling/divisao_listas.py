def divide_colunas(lista1, lista2: list) -> list:
    
    if len(lista1) != len(lista2):
        raise ValueError('As listas tem que ter o mesmo tamanho')

    lista_final = []

    try:
        for i in range(len(lista1)):
            calculo = round(lista1[i] / lista2[i],1)
            lista_final.append(calculo)
            
    except ZeroDivisionError:
        print('Não é possível dividir um número por zero')

    else:
        print('Calculo bem sucedido')

    return lista_final

pressoes = [100, 120, 140, 160, 180]
temperaturas = [0, 25, 30, 35, 40]

try:
    print(divide_colunas(pressoes,temperaturas))

except ValueError as e:
    print(e)