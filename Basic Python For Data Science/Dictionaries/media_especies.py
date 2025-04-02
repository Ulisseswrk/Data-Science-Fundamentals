maior_valor = 0
area = 0
contador = 1

dados = {'Área Norte': [2819, 7236],
 'Área Leste': [1440, 9492],
 'Área Sul': [5969, 7496],
 'Área Oeste': [14446, 49688],
 'Área Centro': [22558, 45148]}

for zona, especie in dados.items():

    soma = sum(especie)
    media = soma / len(especie)

    if maior_valor < media:
        maior_valor = media
        area = zona

    print(f'{zona}:\t {media} de especies')
print(f'\nA area com maior média é a {zona} com {maior_valor}')