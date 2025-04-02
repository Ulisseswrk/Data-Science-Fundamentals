def verificador(certas,notas:list) -> int:
    pontos = 0
    contador = 0

    try:
        for nota in notas:
            if nota in certas[contador]:
                pontos += 1
            contador += 1

    except TypeError:
        print('A lista só pode conter letras')
        return 0
    
    except IndexError:
        print('A lista tem que ter o mesmo número de caracteres que a do gabarito')
        return 0
    
    else:
        return pontos

gabarito = ['A','B','C','D','E']

aluno1 = ['C','D','C','B','E']
aluno2 = ['A','B','D','D','D']
aluno3 = ['A','B','C','D','E']

print(verificador(gabarito,aluno2))