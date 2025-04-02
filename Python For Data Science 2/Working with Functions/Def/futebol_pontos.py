def calcula_pontos(x,y):
    pontos = 0
    aproveitamento = 0

    for i in range(len(x)):
        
        if x[i] > y[i]:
            pontos += 3
        elif x[i] == y[i]:
            pontos += 1
        else:
            pontos += 0
    
    pontos_possiveis = 3*len(x)

    aproveitamento = (pontos / pontos_possiveis) * 100
    return pontos, aproveitamento

gols_marcados = [2, 1, 3, 1, 0]
gols_sofridos = [1, 2, 2, 1, 3]

pontos, aproveitamento = calcula_pontos(gols_marcados, gols_sofridos)
print(f"O time obteve {pontos} pontos e um aproveitamento de {round(aproveitamento,1)}%")