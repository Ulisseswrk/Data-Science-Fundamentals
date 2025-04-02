funcionarios = [('SP', 16), ('ES', 8), ('MG', 9), ('MG', 6), ('SP', 10), ('MG', 4), ('ES',9), ('ES', 7), ('ES', 12), ('SP', 7), ('SP', 11), ('MG',8), ('ES',8), ('SP',9), ('RJ', 13), ('MG', 5), ('RJ', 9), ('SP', 12), ('MG', 10), ('SP', 7), ('ES', 14), ('SP', 10), ('MG', 12)]

estados_unicos = ('SP','ES','MG','RJ')
dicionario = []

for estado in estados_unicos:
    
    separador = sum([(i[1]) for i in funcionarios if i[0] == estado]) #Faz a soma de todos os números de cada estado
    juncao = {estado:separador} #Faz a junção do nome do estado com o total e cria um dict

    dicionario.append(juncao) # Une os resultados em uma lista de dicionarios

print(dicionario)