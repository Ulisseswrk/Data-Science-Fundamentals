qntd_total = 0
media_setor = 0
soma_setor = 0

media_geral = 0
soma_geral = 0
acima_media = 0

idades_setor = {'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
                'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
                'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
                'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}

for setor, idade in idades_setor.items():
    qntd_total += len(idade)

    soma_setor = sum(idade)
    soma_geral += soma_setor

    media_setor = soma_setor / len(idade)

    print(f'A média do {setor} é:\t\t{media_setor}')
    
    for i in idade:
        if i > media_geral:
            acima_media += 1

media_geral = soma_setor / qntd_total

print(f'\nA média geral é:\t\t{round(media_geral, 2)}')
print(f'\nEnquanto há {acima_media} pessoas acima da idade média')