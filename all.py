#print("Olá mundo!")""
#n1 = []
#n2 = []
#for i in range(2):
    #numero = int(input(f"Digite o {i+1}° número: "))
    #if i == 0:
        #n1.append(numero)
    #elif i == 1:
        #n2.append(numero)
#soma = n1[0] + n2[0]
#print(f"A soma de {n1} com {n2} é de:{soma}")
    #numeros.append(numero)
#print(numeros)
#print(f"A soma do número {numeros[0]} e {numeros[1]} é: {soma}")
#n = int(input("Digite um número: "))
#if n % 2 == 0:
    #print("Esse número é par: ")
#else:
    #print("Esse número é impar")
#numero = 0
#n = int(input("Digite um número para saber sua tabuada: "))
#for i in range(1,11,1):
    #i+1
    #print(n*i)
#for i in range(1,11):
    #i+1
    #print(i) 
#soma = 0
#numeros = []
#for i in range (3):
    #n = int(input(f"Diga a sua {i+1}° nota: "))
    #numeros.append(n)
    #soma += n/3
#print(f"Sua primeira nota foi: {numeros[0]}\nSua segunda foi: {numeros[1]}\nSua terceira foi: {numeros[2]}\nA média foi: {soma}")
#num = []
#for i in range(3):
    #n = int(input(f"Diga o {i+1}° número: "))
    #num.append(n)
#if num[0] > num[1] and num[0] > num[2]:
    #print(f"O maior é o {num[0]}")
#elif num[1] > num[0] and num[1] > num[2]: 
    #print(f"O maior é o {num[1]}")
#elif num[2] > num[0] and num[2] > num[1]:
   #print(f"O maior é o {num[2]}")
#if num[2] < num[0] and num[2] < num[1]:
    #print(f"O menor é o {num[2]}")
#elif num[1] < num[0] and num[1] < num[2]:
    #print(f"O menor é o {num[1]}")
#elif num[0] < num[1] and num[0] < num[2]:
    #print(f"O menor é o {num[0]}")
#numeros = []
#for i in range(2):
    #n = int(input(f"Digite o {i+1}° número: "))
    #numeros.append(n)
#fat1 = 1
#fat2 = 1
#while numeros[0] > 0:
    #fat1 *=  numeros[0]
    #numeros[0] -= 1
#while numeros[1] > 0:
    #fat2 *= numeros[1]
    #numeros[1] -= 1
#print(f"O fatorial do 1° número é: {fat1} e do 2° é: {fat2}")
#def calculo_potencia(base,exp):
    #potencia = base ** exp
    #return potencia
#base = int(input("Digite um número como base: "))
#exp = int(input("Digite um número como expoente: "))
#print(calculo_potencia(base,exp))
#def impar_par(n):
    #if n % 2 == 0:
        #return "par"
    #else:
        #return "impar"
#for i in range(5):
    #n = int(input(f"Digite o {i+1}° número: "))
    #print(f"O número {n} é {impar_par(n)}")        ""
#def identificacao_num_primo(n):
    #if n < 2:
        #return "Não é Primo"
    #for i in range(2,n):
        #if n % i == 0:
            #return "Não é primo"
    #return "Primo"
#n = int(input("Digite um número: "))
#print(f"O número {n} é {identificacao_num_primo(n)}")
#def numero_primo(n):
    #if n < 2:
        #return "Não é Primo"
    #numsnaoprimos.append(n)
    #for i in range(2,n):
        #if n % i == 0:
            #numsnaoprimos.append(n)
    #numsprimos.append(n)
    ##return
#numsprimos = []
#numsnaoprimos = []
#n = int(input("Digite um número para saber o maior numero primo menor que n: "))
#print(max(numsprimos))
#n = (input("Digite um número de 4 digitos: "))
#for i in n: 
    #print(i)
#def funcao_media(notas):
    #soma =  (notas[0] + notas[1] + notas[2]) / 3
    #return soma
#notas = []
#for i in range(3):
    #nota = float(input(f"Digite a sua {i+1} nota: "))
    #notas.append(nota)
#print(f"A sua média final foi de:{funcao_media(notas)}")
#notas = 0
#for i in range(3):
    #n = float(input(f"Digite sua {i+1}° nota: "))
    #notas += n
#print(notas/3)
#FATORIALLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL
#calc = 1 # Igual a um pq não existe multiplicação por 0
#n = int(input("Digite um número para saber seu fatorial: ")) # input padrão
#for i in range (1, n+1): #laco for usando o comeco 1 ao inves do 0 e n+1 ja que ele sempre para um num antes
#calc *= i # adicionando a uma variavel e automaticamente multiplicando-a
#print(calc) #resultados
#PRIMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#n = int(input("Digite um número para saber se é primo: "))
#if n < 2:
    #print("Não é primo C1")
#else:
    #eprimo = True
#for i in range(2,n):
    #if n % i == 0:
        #print("Não é primo C2")
    #break
#if eprimo:
    #print("É primo C3")
#num = int(input("Digite um numero: "))
#r = 1
#for i in range (1,num+1):
    #r *= i
#print(r)
#num = int(input("Digite um número para saber se é primo: "))
#if num < 2:
   #print("Não é primo C1")
#for i in range(2,num):
    #if num % i == 0:    
        #print("Não é primo C2")
        #break
#else:
    #print("É primo C3")
#def calculo_media (numeros):
    #resultado =  (numeros[0] + numeros[1] + numeros[2]) / 3
    #return resultado° número: "))
    #numeros.append(n)
#numeros = []
#for i in range(3):
    #n = int(input(f"Digite o {i+1}
#print(calculo_media(numeros))
#resultado = 1
#n = int(input("Digite um número para saber seu fatorial: "))
#for i in range(1,n+1):
   #resultado *=  i
#print(resultado)
#while True:
    #n = int(input("Digite um número: "))
    #if n < 2:
        #print("Não é primo C1")
        #continue
    #for i in range (2,n):
        #if n % i == 0:
            #print("Não é primo C2")
            #break
    #else:
        #print("É primo C3")
        #break
#result = 1
#n = int(input("Digite um número: "))
#for i in range(1,n+1):
    #result *= i
#print(result)
#n = int(input("Digite um número: "))
#if n < 2:
    #print("Não é primo C1")
#for i in range(2,n):
    #if n % i == 0:
        #print("Não é primo C2")
        #break
#else:
    #print("É primo")
#n = int(input("Digite um número: "))
#resultado = 1
#for i in range(1,n+1):
    #resultado *=  i
#print(resultado)
#while True:
#n = int(input("Digite um número: "))
#if n < 2:
     #print("Não é primo C1")
    #continue
#for i in range(2,n):
    #if n % i == 0:
        #print("Não é primo")
        #break
#else:
        #print("É primo C3")
#resultado = 1
#n = int(input("Digite um número: "))
#for i in range(1,n+1):
    #resultado *= i
#print(resultado)
#while True:
    #n = int(input("Digite um número: "))
    #if n < 2:
        #print("Não é primo C1")
        #continue
    #for i in range(2,n):
        #if n % i == 0:
            #print("Não é primo C2")
            #break
    #else:
        #print("É primo C3")
    #break
#txt = "ulisses ribeiro abreu"
#txt = txt.replace("ulisses ribeiro abreu","Ulisses Riyeiro abreu")
#print(txt)
#teste = input("Digite alguma coisa: ")
#if type(teste) == str:
    #print("é uma string")
#else:
    #print("erro")
#nome = input("Digite seu nome: ")
#idade = int(input("Digite a sua idade: "))
#altura = str(input("Digite sua altura: ")).replace(",",".")
#altura = float(altura)
#print(f"Nome:\t{nome}\nIdade:\t{idade}\nAltura:\t{altura}")
#num1 = int(input("Digite um número: "))
#num2 = int(input("Digite um número: "))
#numeros = [num1,num2]
#print(max(numeros))
#porcentagem = input("Digite o percentual de crescimento da empresa: ")
#porcentagem = int(porcentagem.strip("%"))
#if porcentagem >= 1:
    #print("Positivo!")
#else:
    #print("Negativo")
#letra = input("Digite uma letra para descobrir se é vogal ou consoante: ")
#letra = letra.upper()
#if letra in "AEIOU":
    #print("Vogal")
#else:
    #print("Consoante")
#value = []
#for i in range(3):
    #numeros = float(input(f"Escreva o {i+1}º valor médio de preço: "))
    #value.append(numeros)
#print(f"\nO maior valor é: {str(max(value)).replace(".",",")}\nO menor é: {str(min(value)).replace(".",",")}" )
#mercado = []
#for i in range(3):
    #dados = str(input("Digite o nome de um produto e em seguida seu preço: "))
    #mercado.append(dados)
    #if i == 0 or i == 1:
        #print("Produto Cadastrado!")
    #else:
       #print("")
#print(f"Dentre esses produtos, o mais barato pra se comprar é o: {min(mercado)}")
#nums = []
#ordem = []
#for i in range(3):
    #num = input(f"Digite o {:i+1}º número: ")
    #nums.append(num)
#for i in range(3):
    #ordem.append(max(nums))
    #nums.remove(max(nums))
#print(ordem)
#while True:
    #turno = input("Informe seu turno: ")
    #turno = turno.upper()
    #if turno == "MANHA" or turno == "MANHÃ":
        #print("Bom dia")
        #break
    #elif turno == "TARDE":
        #print("Boa Tarde")
        #break
    #elif turno == "NOITE":
        #print("Boa noite")
        #break
    #else:
        #print("Valor Invalido")
#num = int(input("Informe um número: "))
#if num % 2 == 0:
    #print("O número é par")
#else:
    #print("Impar")
#num = float(input("Informe um número: "))
#if num % 1 == 0:
    #print("Inteiro")
#else:
    #print("Decimal")
#numeros = []
#for i in range(2):
    #num = float(input(f"Digite o {i+1}º número: "))
    #numeros.append(num)
#while True:
    #funcao = int(input("\nDigite 1 para par e impar:\nDigite 2 para positivo ou negativo:\nDigite 3 para inteiro ou decimal: "))
    #if funcao < 1 or funcao > 3:
        #print("Digite um número válido e tente novamente")
        #continue
    #else:
        #break
#if funcao == 1:
    #if numeros[0] % 2 == 0 and numeros[1] % 2 != 0:
        #print("O primeiro número é par e o segundo impar")
    #elif numeros[0] % 2 != 0 and numeros[1] % 2 == 0:
       #print("O primeiro número é impar e o segundo par")
    #elif numeros[0] % 2 == 0 and numeros[1] % 2 == 0:
        #print("Ambos os números são par")
    #else:
        #print("Ambos os números são impar")
#elif funcao == 2:
    #if numeros[0] >= 1 and numeros[1] < 1:
        #print("O primeiro número é positivo e o segundo negativo")
    #elif numeros[0] < 1 and numeros[1] >= 1:
        #print("O primeiro número é negativo e o segundo positivo")
    #elif numeros[0] >= 1 and numeros[1] >= 1:
        #print("Ambos os números são positivos")
    #elif 1 > numeros[0] != 0 and 1 > numeros[1] != 0:
        #print("Ambos os números são negativos")
    #elif numeros[0] == 0 and numeros[1] < 1:
        #print("O primeiro número é neutro e o segundo negativo")
    #elif numeros[0] == 0 and numeros[1] >= 1:
        #print("O primeiro número é neutro e o segundo positivo")
    #elif numeros[0] < 1 and numeros[1] == 0:
        #print("O primeiro número é negativo e o segundo neutro")
    #elif numeros[0] >= 1 and numeros[1] == 0:
        #print("O primeiro número é positivo e o segundo neutro")
    #else:
        #print("Ambos os números são neutros")
#elif funcao == 3:
    #if numeros[0] % 1 == 0 and 0 < (numeros[1] % 1) > 0:
        #print("O primeiro número é inteiro e o segundo decimal")
    #elif 0 < (numeros[0] % 1) > 0 and numeros[1] % 1 == 0:
        #print("O primeiro número é decimal e o segundo inteiro")
    #elif 0 < (numeros[0] % 1) > 0 and 0 < (numeros[1] % 1) > 0:
        #print("Ambos os números são decimais")
    #elif numeros[0] % 1 == 0 and numeros[1] % 1 == 0: 
        #print("Ambos os números são inteiros")
#num1 = int(input("Digite o 1º número: "))
#num2 = int(input("Digite o 2º número: "))
#for i in range(num1,num2+1):
    #num1 += 1
    #print(i)
#coloniaa = 4
#coloniab = 10
#contador = 0
#while coloniaa <= coloniab:
    #coloniaa *= 1 + 0.030
    #coloniab *= 1 + 0.015
    #contador += 1
#print(contador)
#contador = 1
#verificacao = True
#while verificacao == True:
    #dados = float(input(f"Digite a {contador}º nota: "))
    #contador += 1
    #if dados > 5 or dados < 0:
       #print("\nDigite um número entre 0 a 5\n")
        #contador = 1
    #elif contador == 16:
        #print("Obrigado por colaborar, fim")
        #break
#soma = 0
#contador = 0
#temperatura = float(input("Digite uma temperatura: "))
#while temperatura != -273:
    #soma += temperatura
    #contador += 1
    #temperatura = float(input("Digite uma temperatura: "))
#media = soma / contador
#print(f"A média das temperaturas é: {media}")
#fatorial = 1
#num = int(input("Digite um número: "))
#for i in range(1,num+1):
    #fatorial *= i
#print(fatorial)
#num = int(input("Digite um número: "))
#if num < 2:
    #print("Não é primo C1")
#for i in range(2,num):
    #if num % i == 0:
        #print("Não é primo C2")
#print("É primo C3")
#num = int(input("Digite um número: "))
#for i in range(1,11):
    #print(f"{num} x {i} = {num*i}")
#g1 = 0
#g2 = 0
#g3 = 0
#g4 = 0
#idade = int(input("Informe sua idade: "))
#while idade > 0:
    #idade = int(input("Informe sua idade: "))
    #if 25 >= idade > 0:
        #g1 += 1
    #elif 50 >= idade >= 26:
        #g2 += 1
    #elif 75 >= idade >= 51:
        #g3 += 1
    #elif 100 >= idade >= 76:
        #g4 += 1
#print(f"\nSua empresa tem:\n{g1} pessoas até 25\n{g2} pessoas até 50\n{g3} pessoas até 75\n{g4} pessoas até 100 anos")
#v1 = 0
#v2 = 0 
#v3 = 0 
#v4 = 0 
#nulo = 0 
#branco = 0
#tot = 0
#for i in range(1,22):
    #voto = int(input("Escolha seu candidato de 1 a 4 (5 nulo e 6 branco)\n\nDigite seu voto: "))
    #if voto == 1:
        #v1 += 1
    #if voto == 2:
        #v2 += 1
    #if voto == 3:
        #v3 += 1
    #if voto == 4:
        #v4 += 1
    #if voto == 5:
        #nulo += 1
    #if voto == 6:
        #branco += 1
#cbranco = (branco / 20) * 100
#cnulo = (nulo / 20) * 100
#print(f"\nRESULTADO DAS ELEIÇÕES:\n{v1} para candidato 1\n{v2} para candidato 2\n{v3} para candidato 3\n{v4} para candidato 4\n{nulo} votos nulos\n{branco} votos branco\nOs votos nulos representaram {cnulo}% dos votos e os brancos {cbranco}%")
#gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.0]
#tot_gastos = len(gastos)
#soma = sum(gastos)
#print(f"O total dos gastos foi de: {len(gastos)}\nEnquanto a média foi: {soma / tot_gastos}")
#gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.0]
#maiores = []
#for gasto in gastos:
    #if gasto >= 3000:
        #maiores.append(gasto)
#print(f"A média dos maiores foi de: {round(sum(maiores) / len(maiores), 2)}")
#numeros = []
#for i in range(5):
    #num = int(input(f"Digite o {i+1}º numeros: "))
    #numeros.append(num)
#print(numeros)
#numeros = []
#for i in range(5):
    #num = int(input(f"Digite o {i+1}º numeros: "))
    #numeros.append(num)
#print(numeros[::-1])

#primos = []
#num = int(input("Digite um número: "))

#Gera a sequencia de numeros
#for numero in range(2,num):
    #eprimo = True
    #for i in range(2,numero):
        #f numero % i == 0:
           #eprimo = False
            #break
    #if eprimo:
        #primos.append(numero)
#print(primos)
#contador = 0
#while True:
    #meses = ("JANEIRO","FEVEREIRO","MARCO","ABRIL","MAIO","JUNHO","JULHO","AGOSTO","SETEMBRO","OUTUBRO","NOVEMBRO","DEZEMBRO")
    #meses_30_dias = ["ABRIL", "JUNHO", "SETEMBRO", "NOVEMBRO"]
    #dia = int(input("Informe um dia: ").strip())
    #mes = input("Informe um mês: ").strip().upper()
    #ano = int(input("Informe um ano: ").strip())
    #contador += 1
    #if contador == 3:
        #sair = input("Digite S/N para sair").strip().upper()
        #if sair == "SIM":
            #break
    #if contador == 1:
        #print("")
    #if dia < 1 or dia > 31:
        #print("Dia inválido")
        #continue
    #if ano > 2025:
        #print("Ano inválido")
        #continue
    #if mes in meses[2:11] and dia > 13 and ano == 2025:
        #print("Essa data ainda não chegou")
        #continue
    #if mes not in meses:
        #print("Esse mes não existe")
        #continue
    #if mes in meses_30_dias and dia > 30:
        #print("Esse mes não tem 31 dias, tente novamente:\n")
        #continue
    #if mes == "FEVEREIRO" and dia == 29:
        #if (ano % 4 != 0) and (ano % 100 == 0 and ano % 400 != 0):
            #print("O ano não é bissexto, logo fevereiro não tem 29 dias")
            #continue
    #else:
        #print("Obrigado por colaborar, fim do código.")
    #break
#primos = []
#num = int(input("Digite um número: "))
#for i in range(2,num):
    #eprimo = True
    #for numero in range(2,i):
        #if i % numero == 0:
            #eprimo = False
            #break
    #else:
        #primos.append(i)
#print(primos)
#bacterias = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]
#crescimentos = []
#for i in range(1,len(bacterias)):
    #crescimento =  round(100 * (bacterias[i] - bacterias[i-1]) / (bacterias[i-1]), 2)
    #crescimentos.append(crescimento)
#print(f"O crecimento por dia de {crescimentos}")
#doces = []
#amargos = []
#for i in range(0,10):
    #id = int(input(f"Digite o {i+1}º ID: ").strip())
    #if id % 2 == 0:
        #doces.append(id)
    #else:
        #amargos.append(id)
#print(f"Diante desses dados:\nTemos: {len(doces)} doces\t {len(amargos)} amargos")
#notas = []
#gabarito = ["D","A","C","B","A","D","C","C","A","B"]
#certas = 0
#for i in range(0,10):
    #notas.append(input(f"Digite a resposta da {i+1}º questão: ").strip().upper())
    #if notas[i] == gabarito[i]:
        #certas += 1
#print(certas)
#temps = []
#maiores_temperaturas = []
#for i in range(0,12):
    #temps.append(float(input(f"Digite a {i+1}º temperatura: ").strip()))
#media = sum(temps) / len(temps)
#for temperatura in temps:
    #if temperatura > media:
        #maiores_temperaturas.append(max(temps))
        #temps.remove(max(temps))
#print(f"A média das temperaturas anuais foram: {media}\nPor outro lado, as maiores temperaturas foram: {maiores_temperaturas}")
#prods = {'Produto A': 300, 'Produto B': 80, 'Produto C': 60,
         #'Produto D': 200, 'Produto E': 250, 'Produto F': 30}
#maior_venda = 0
#produto_mais_vendido = 0
#for i in prods.keys():
    #if maior_venda < prods[i]:
        #maior_venda = prods[i]
        #produto_mais_vendido = i
#print(f"O total de vendas foi: {sum(prods.values())}\nEnquanto o produto mais vendido foi: {produto_mais_vendido}, com {maior_venda} vendas efetuadas")
#dados = {'Produto A': 300, 'Produto B': 80, 'Produto C': 60,
#'Produto D': 200, 'Produto E': 250, 'Produto F': 30}
#nome = 0
#maior_numero = 0
#for dado in dados.keys():
    #if maior_numero < dados[dado]:
        #maior_numero = dados[dado]
        #nome = dado
#print(f"O número total de vendas foi de: {sum(dados.values())}\nO produto mais vendido foi o {nome} com {maior_numero} de vendas ")
#mais_votado = 0
#design_favorito = 0
#votos = {'Design 1': 1334,'Design 2': 982,'Design 3':  1751,'Design 4': 210,'Design 5': 1811, }
#for voto in votos.keys():
    #if mais_votado < votos[voto]:
        #mais_votado = votos[voto]
        #design_favorito = voto
#porcentagem = (mais_votado / sum(votos.values()) * 100)
#print(f"\nDentre as opções:\n{", ".join(votos.keys())}", end = ".")
#print(f"\n\nO mais votado foi: {design_favorito} com {mais_votado}\nRepresentando assim: {round(porcentagem,2)}% dos votos.")
#abono_minimo = 0
#salarios_abono = {1172:200, 1644:200, 2617:260, 5130:510, 5532:553, 
                  #6341:634, 6650:665, 7238:723, 7685:768, 7782:772, 7903:790}
#gasto_abono = sum(salarios_abono.values())
#for abono in salarios_abono.values():
    #if abono == 200:
        #abono_minimo += 1
#print(f"O gasto total com abono foi: {gasto_abono}\n"
      #f"O número de pessoas que pegou o minimo de abono foi: {abono_minimo}\n"
      #f"O número maximo de abono recebido foi: {max(salarios_abono.values())}")
#maior_valor = 0
#area = 0
#contador = 1
#dados = {'Área Norte': [2819, 7236],
 #'Área Leste': [1440, 9492],
 #'Área Sul': [5969, 7496],
 #'Área Oeste': [14446, 49688],
 #'Área Centro': [22558, 45148]}
#for zona, especie in dados.items():
    #soma = sum(especie)
    #media = soma / len(especie)
    #if maior_valor < media:
        #maior_valor = media
        #area = zona
    #print(f'{zona}:\t {media} de especies')
#print(f'\nA area com maior média é a {zona} com {maior_valor}')
#qntd_total = 0
#media_setor = 0
#soma_setor = 0
#media_geral = 0
#soma_geral = 0
#acima_media = 0
#idades_setor = {'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
                #'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
                #'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
                #'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}
#for setor, idade in idades_setor.items():
    #qntd_total += len(idade)
    #soma_setor = sum(idade)
    #soma_geral += soma_setor
    #media_setor = soma_setor / len(idade)
    #print(f'A média do {setor} é:\t\t{media_setor}')
    #for i in idade:
        #if i > media_geral:
            #acima_media += 1
#media_geral = soma_setor / qntd_total
#print(f'\nA média geral é:\t\t{round(media_geral, 2)}')
#print(f'\nEnquanto há {acima_media} pessoas acima da idade média')
#import matplotlib.pyplot as plt
#estudantes = ['Ulisses', 'Eduardo','Antonio']
#notas = [10,5,7.5]
#plt.bar(x = estudantes, height = notas)
#plt.show()
#from random import choice
#lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]
#print(f'O número escolhido foi: {choice(lista)}')
#from math import pow
#num1 = int(input('Digite um número: '))
#num2 = int(input('Digite outro número: '))
#print(pow(num1,num2))
#from random import choice
#numero = int(input('Selecione o número de participantes: '))
#lista = list(range(1,numero+1))
#print(f'O número sorteado foi: {choice(lista)}')
#from random import randrange
#tokens = randrange(1000,9999,2)
#nome = input('Digite o seu nome: ')
#print(f'Seu nome é {nome} e seu token é {tokens}')
#from random import choice
#contador = 0
#frutas = ["maçã", "banana", "uva", "pêra", 
          #"manga", "coco", "melancia", "mamão",
          #"laranja", "abacaxi", "kiwi", "ameixa"]
#for i in frutas:
    #if contador == 0:
        #print('Sua salada de frutas será composta por:', end = ' ')
    #print(f'{choice(frutas)}', end = ', ')
    #contador += 1
    #if contador == 2:
        #print(choice(frutas), end = '. ')
        #break
#from random import choices
#frutas = ["maçã", "banana", "uva", "pêra", 
          #"manga", "coco", "melancia", "mamão",
          #"laranja", "abacaxi", "kiwi", "ameixa"]
#escolha = choices(frutas, k=3)
#print(f"A sua salada de frutas vai ser composta por {escolha[0], escolha[1], escolha[2]}.")
#from math import pow
#numeros = [2, 8, 15, 23, 91, 112, 256]
#for i in numeros:
    #if pow(i, 0.5) % 1 == 0 and i <= 100:
        #print(f'A raiz de {i}  =\t\tinteira')
    #elif pow(i, 0.5) % 1 == 0 and i >= 100:
        #print(f'A raiz de {i} =\t\tInteira')
    #elif pow(i, 0.5) % 1 != 0 and i <= 100:
        #print(f'A raiz de {i}  =\t\tDecimal')
#from math import pi, pow
#raio = float(input('Digite o raio da área circular: '))
#area = pi * pow(raio,2)
#print(f'\nO metro quadrado do nosso gramado custa R$ 25,00\n'
      #f'Logo, pela como sua area é {round(area,2)} m², o valor final é: R$ {round(25 * area,2)}')
#lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]
#print(f'A lista tem o tamanho: {len(lista)}\n'
      #f'O maior valor da lista é {max(lista)}\n'
      #f'O menor valor é {min(lista)}')
#def tabuada(num: int) -> int:
    #print(f'\nTabuada do {num}:\n')
    #for i in range(1,11):
        #print(num, 'X', i, '=', num+i)
    #return tabuada
#num = int(input('Digite um número: '))
#print(tabuada(num))
#def divisores(lista):
    #multiplos = []
    #for i in lista:
        #if i % 3 == 0:
            #multiplos.append(i)
    #return multiplos
#lista = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]
#print(divisores(lista)) 
#numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#funcao = list(map(lambda x: pow(x,2), numeros))
#print(funcao)
#def avaliador(x):
    #x.remove(max(x))
    #x.remove(min(x))
    #return sum(x) / len(x)
#notas = []
#for i in range(1,6):
    #nota = float(input('Digite a nota do skatista: '))
    #notas.append(nota)
#print(f'A pontuação do skatista foi: {avaliador(notas)}')
#def calculo(x):
    #x_max = max(x)
    #x_min = min(x)
    
    #media = sum(x) / len(x)
    #if media > 6:
        #return f'A nota maxima do aluno foi {x_max}\nA minima foi {x_min} e ele foi aprovado'
    #else:
        #return f'A nota maxima do aluno foi {x_max}\nA minima foi {x_min} e ele foi reprovado'
#notas = []
#for i in range(4):
    #nota = float(input('Digite a nota do skatista: '))
    #notas.append(nota)
#print(calculo(notas))
#nomes = ["joão", "MaRia", "JOSÉ"]
#sobrenomes = ["SILVA", "souza", "Tavares"]
#identificadora = map(lambda nome, sobrenome: f"{nome.capitalize()} {sobrenome.capitalize()}", nomes, sobrenomes)
#for i in identificadora:
    #print(f"Nome completo: {i}")
#nomes = ["joão", "MaRia", "JOSÉ"]
#sobrenomes = ["SILVA", "souza", "Tavares"]
#funcao = map(lambda x, y: f"{x.capitalize()} {y.capitalize()}", nomes, sobrenomes)
#for i in funcao:
    #print(i)
#def calcula_pontos(x,y):
    #pontos = 0
    #aproveitamento = 0
    #for i in range(len(x)):
        #if x[i] > y[i]:
            #pontos += 3
        #elif x[i] == y[i]:
            #pontos += 1
        #else:
            #pontos += 0
    #pontos_possiveis = 3*len(x)
    #aproveitamento = (pontos / pontos_possiveis) * 100
    #return pontos, aproveitamento
#gols_marcados = [2, 1, 3, 1, 0]
#gols_sofridos = [1, 2, 2, 1, 3]
#pontos, aproveitamento = calcula_pontos(gols_marcados, gols_sofridos)
#print(f"O time obteve {pontos} pontos e um aproveitamento de {round(aproveitamento,2)}%")
#frase = "Aprender Python aqui na Alura é muito bom"
#cidades = ("SALVADOR","FORTALEZA","NATAL","ARACAJU")
#valor_passeios = [200, 400, 250, 300]
#distancias = [850, 800, 300, 550]
#diaria = 150
#consumo = 14
#gasolina = 5
#gasto_total = 0
#def gasto_hotel(diaria: float) -> float:
    #gasto1 = 0
    #gasto1 += diaria
    #return gasto1
#def gasto_gasolina(cidade:str, distancias:list ,consumo:float, gasolina:float) -> float:
    #gasto2 = 0
    #calculo = (distancias[0] / consumo) * gasolina
    #if cidade == "SALVADOR": # É Salvador
        #gasto2 += (distancias[0] / consumo) * gasolina
    #elif cidade == "FORTALEZA": # É Fortaleza
        #gasto2 += (distancias[1] / consumo) * gasolina
    #elif cidade == "NATAL": # É Natal
        #gasto2 += (distancias[2] / consumo) * gasolina
    #elif cidade == "ARACAJU": # É Aracaju
        #gasto2 += (distancias[3] / consumo) * gasolina
    #return gasto2
#def gasto_passeio(valor_passeios:list) -> float:
    #gasto3 = 0
    #for i in range(len(valor_passeios)):
        #if i == 0:
            #gasto3 += valor_passeios[0]
        #elif i == 1:
           #gasto3 += valor_passeios[1]
        #elif i == 2:
            #gasto3 += valor_passeios[2]
        #elif i == 3:
            #gasto3 += valor_passeios[3]
    #return gasto3
#while True: 
    #cidade = input("Digite sua cidade desejada: ").upper()
    #if cidade not in cidades:
        #cidade = input("Cidade inválida, tente novamente: ").upper()
    #else:
        #break
#gasto_total = gasto_hotel(diaria) + gasto_gasolina(cidade, distancias,consumo,gasolina) + gasto_passeio(valor_passeios) 
#print(f"O gasto pra visitar {cidade.capitalize()} é R${round(gasto_total,2)}")
#código extremamente simples mas contém duas funções que eu não costumava usar
#frase = input("Digite uma frase: ")
#frase = frase.replace("."," ").replace(";"," ").replace("^"," ").split()
#selecao = filter(lambda x: len(x) >= 5, frase)
#for i in selecao:
    #print("As palavras que possuem cinco ou mais letras foram: ")
    #print(i)
#frase = input("Digite uma frase para saber as palavras com 5 ou mais letras: ")
#frase = frase.replace(";"," ").replace("^"," ").replace("."," ").split()
#funcao = filter(lambda x: len(x) >= 5, frase)
#for i in funcao:
    #print(i, end = " ")
#lista_precos = [500,200,400,800]
#nova_lista = [preco * 2 for preco in lista_precos]
#lista_imposto = [preco * 0.5 + preco for preco in nova_lista]
#print(nova_lista, lista_imposto)
#pares = [x for i in range(21) if i % 2 == 0]
#print(pares)
#numeros = [1, 2, 3, 4, 5]
#quadrado = [i ** 2 for i in numeros]
#print(quadrado)
#palavras = ["Python", "List", "Comprehension", "Exercicio", "Aprender"]
#palavras_cinco_letras = [i for i in palavras if len(i) > 5]
#print(palavras_cinco_letras)
#palavras = ["ola", "mundo", "python", "programacao"]
#maiusculas = [i.upper() for i in palavras]
#print(maiusculas)
#divisiveis = [i for i in range(1,51) if i % 3 == 0 and i % 5 == 0 ]
#print(divisiveis)
#quadrados_impares = [i ** 2 for i in range(1,50,2) if i % 5 != 0 ]
#print(quadrados_impares)
#palavras = ["banana", "abacate", "python", "exercicios", "algoritmo", "lista"]
#lista_invertida = [i[::-1] for i in palavras if len(i) % 2 == 0]
#print(lista_invertida)
#meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
#despesa = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360]
#dicionario = {meses[i]:despesa[i] for i in range(len(meses))}
#print(dicionario)
#aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]
#valor_apartamentos = [i for i in aluguel if i[0] == 'Apartamento']
#print(valor_apartamentos)
#lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo']
#lista_certa = []
#for i in range(len(lista)):
#     lista_certa.append((i, lista[i]))
#print(lista_certa)
#lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]
#lista_nova = [i[2] for i in lista_de_tuplas]
#print(lista_nova)
#lista_de_listas = [[4,6,5,9], [1,0,7,2], [3,4,1,8]]
#lista_nova = [sum(i) for i in lista_de_listas]
#print(sum(lista_nova))
#vendas = [('2023', 4093), ('2021', 4320), ('2021', 5959), ('2022', 8883), ('2023', 9859), ('2022', 5141), ('2022', 7688), ('2022', 9544), ('2023', 4794), ('2021', 7178), ('2022', 3030), ('2021', 7471), ('2022', 4226), ('2022', 8190), ('2021', 9680), ('2022', 5616)]
#vendas_22 = [i[1] for i in vendas if i[0] == '2022' and i[1] >= 6000]
#print(vendas_22)
#glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]
#lista = [('Hipoglicemia', i) if i <= 70 else ('Normal',i) if 99 >= i > 70 else('Alterada',i) if 125 >= i > 100 else ('Diabetes',i) for i in glicemia]
#print(lista)
#lista = [('Hipoglicemia', i) if i <= 70 else ('Normal', i) if 99 >= i > 70 else ('Alterada', i) if 125 >= i > 100 else ('Diabetes', i) for i in glicemia]
#rotulos = [('Hipoglicemia', i) if i <= 70 else ('Normal', i), if i < 100 else ('Alterada', i), if i < 125 else ('Diabetes', i), for i in glicemia]
#glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]
#lista = [('Hipoglicemia') if i <= 70 else ('Normal') if 99 > i > 70 else ('Alterada') if 125> i > 100 else ('Diabetes') for i in glicemia]
#print(lista)
#id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#quantidade = [15, 12, 1, 15, 2, 11, 2, 12, 2, 4]
#preco = [93.0, 102.0, 18.0, 41.0, 122.0, 14.0, 71.0, 48.0, 14.0, 144.0]
#lista_de_tuplas = ['IDs','Quantidade', 'Preco', 'Preco Total']
#lista_de_tuplas += [(id[i], quantidade[i], preco[i], preco[i] * quantidade[i]) for i in range(len(id))]
#print(lista_de_tuplas)
#estados_repetidos = ['SP', 'ES', 'MG', 'MG', 'SP', 'MG', 'ES', 'ES', 'ES', 'SP', 'SP', 'MG', 'ES', 'SP', 'RJ', 'MG', 'RJ', 'SP', 'MG', 'SP', 'ES', 'SP', 'MG']
#estados_unicos = list(set(estados_repetidos))
#lista_de_lista = []
#for estado in estados_unicos:
    #lista = [i for i in estados_repetidos if i == estado]
    #lista_de_lista.append(lista)
#dict_comprehension = {estados_unicos[i]:len(lista_de_lista[i]) for i in range(len(estados_unicos))}
#print(dict_comprehension)
#estados_repetidos = ['SP', 'ES', 'MG', 'MG', 'SP', 'MG', 'ES', 'ES', 'ES', 'SP', 'SP', 'MG', 'ES', 'SP', 'RJ', 'MG', 'RJ', 'SP', 'MG', 'SP', 'ES', 'SP', 'MG']
#estados_unicos = list(set(estados_repetidos))
#lista_listas = []
#for estado in estados_unicos:
    #lista = [i for i in estados_repetidos if i == estado]
    #lista_listas.append(lista)
#dicionario_estados = {estados_unicos[i]:len(lista_listas[i]) for i in range(len(estados_unicos))}
#print(dicionario_estados)
#fatorial = 1
#num = int(input('Digite um número para saber seu fatorial: '))
#calculo = 0
#for i in range(1,num+1):
    #fatorial *= i
#print(fatorial)
#funcionarios = [('SP', 16), ('ES', 8), ('MG', 9), ('MG', 6), ('SP', 10), ('MG', 4), ('ES',9), ('ES', 7), ('ES', 12), ('SP', 7), ('SP', 11), ('MG',8), ('ES',8), ('SP',9), ('RJ', 13), ('MG', 5), ('RJ', 9), ('SP', 12), ('MG', 10), ('SP', 7), ('ES', 14), ('SP', 10), ('MG', 12)]
#estados_unicos = ('SP','ES','MG','RJ')
#dicionario = []
#for estado in estados_unicos:
    #separador = sum([(i[1]) for i in funcionarios if i[0] == estado]) #Faz a soma de todos os números de cada estado
    #juncao = {estado:separador} #Faz a junção do nome do estado com o total e cria um dict
    #dicionario.append(juncao) # Une os resultados em uma lista de dicionarios
#print(dicionario)
#try:
    #n1 = float(input('Digite um número: '))
    #n2 = float(input('Digite outro número: '))
    #divisao = n1 / n2
#except ValueError:
    #print('O valor deve ser um número inteiro para efetuar a divisão')
#except ZeroDivisionError:
    #print('O segundo número não pode ser 0')
#else:
    #print(divisao)
#idades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}
#try:
    #idade = input('Digite um nome: ').capitalize()
    #resultado = idades[idade]
#except KeyError:
    #print('Esse nome não está na lista')
#else:
    #print(resultado)
#def transformador(lista: list) -> float:
        #for numero in lista:
            #print(float(numero))
        #return ''
#try: 
    #numeros = [1,2,3,4,5,6,7,8,9,x]
    #print(transformador(numeros))
#except TypeError:
    #print('O número tem que ser int')
#except NameError:
    #print('O número n pode ser uma variavel')
#finally:
     #print('Fim do código.')
#def agrupador(l1,l2:list) -> list:
    #try:
        #dados = [(l1[i], l2[i], l1[i]+l2[i]) for i in range(len(l1))]
    #except IndexError:
        #print('Uma das listas é maior que a outra') #In case of one of the list being bigger than the other
    #except TypeError:
        #print('A lista só pode ter números') #If someone inserting a string at the list
    #except NameError:
        #print('A não pode ter variaveis') #In case of someone inserting an a at the list without the '' for example
    #else:
        #return dados
    #finally: 
        #return 'Fim do Programa' #The end of the function
#lista1 = [1,2,3,4,5,6,7,8,9,10,]
#lista2 = [6,5,7,3,5,4,7,6,8,70]
#print(agrupador(lista1,lista2))
#lista_dupla = list(zip(lista1,lista2))
#print(lista_dupla)]
#def verificador(certas,notas:list) -> int:
    #pontos = 0
    #contador = 0
    #try:
        #for nota in notas:
            #if nota in certas[contador]:
                #pontos += 1
            #contador += 1
    #except TypeError:
        #print('A lista só pode conter letras')
        #return 0
    #except IndexError:
        #print('A lista tem que ter o mesmo número de caracteres que a do gabarito')
        #return 0
    #else:
        #return pontos
#gabarito = ['A','B','C','D','E']
#aluno1 = ['C','D','C','B','E']
#aluno2 = ['A','B','D','D','D']
#aluno3 = ['A','B','C','D','E']
#print(verificador(gabarito,aluno2))
#def removedor(lista:list) -> list:
    #for i in lista:
        #if ":" in i or ";" in i:
            #return i
    #return ""
#frase = "A tecnologia evolui: rapidamente; transformando o mundo ao nosso redor."
#lista_palavras = frase.split()
#frase_corrigida = removedor(lista_palavras).replace(":","").replace(";","")
#try:
    #if ":" in removedor(lista_palavras) or ";" in removedor(lista_palavras):
        #raise ValueError("A frase não pode conter caracteres especiais")
#except ValueError as e:
    #print(f"Caracteres especiais foram usados após a palavra {frase_corrigida}. {e}")
#else:
    #print("A palavra não tem caracteres especiais")
#finally:
    #print("Fim do código")
#def divide_colunas(lista1, lista2: list) -> list:

    #if len(lista1) != len(lista2):
        #raise ValueError('As listas tem que ter o mesmo tamanho')
    #lista_final = []
    #try:
        #for i in range(len(lista1)):
            #calculo = round(lista1[i] / lista2[i],1)
            #lista_final.append(calculo)
    #except ZeroDivisionError:
        #print('Não é possível dividir um número por zero')
    #else:
        #print('Calculo bem sucedido')
    #return lista_final
#pressoes = [100, 120, 140, 160, 180]
#temperaturas = [0, 25, 30, 35, 40]
#try:
    #print(divide_colunas(pressoes,temperaturas))
#except ValueError as e:
    #print(e)
#import numpy as np
#url = 'https://raw.githubusercontent.com/Marina-Falcao-DEV/apples_ts.csv-Alura-_-Numpy-/refs/heads/main/apples_ts.csv'
#dado = np.loadtxt(url,delimiter=',',usecols=np.arange(1,88,1)) #separa os dados por , e comeca da primeira coluna numeral
#dado_transposto = dado.T
#dado.size # 522
#dado.shape # 6, 87
#dado.ndim #dimensoes 2
#import numpy as np
#url = 'https://raw.githubusercontent.com/allanspadini/numpy/dados/citrus.csv'
#arquivo = np.loadtxt(url,delimiter=',', usecols=np.arange(1,6,1), skiprows=1)
#print(arquivo)
import numpy as np
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/Marina-Falcao-DEV/apples_ts.csv-Alura-_-Numpy-/refs/heads/main/apples_ts.csv'
dado = np.loadtxt(url,delimiter=',',usecols=np.arange(1,88,1)) #separa os dados por , e comeca da primeira coluna numeral
dado_transposto = dado.T

datas = dado_transposto[:, 0] # pega todo o intervalo de linhas anteriores
precos = dado_transposto[:, 1:6]

moscow = precos[:,0]
kaliningrad = precos[:,1]
petersburg = precos[:,2]
krasnodar = precos[:,3]
ekaterinburg = precos[:,4]

moscow_ano1 = moscow[0:12]
moscow_ano2 = moscow[12:24]
moscow_ano3 = moscow[24:36]
moscow_ano4 = moscow[36:48]

plt.plot(datas,kaliningrad)
kaliningrad[4] =  np.mean([kaliningrad[3],kaliningrad[5]])
print(kaliningrad)



















#datas = np.arange(1,88,1)
#plt.plot(datas, precos[:,0])
#plt.title('Gráfico de aumento dos preços')
#plt.xlabel('Datas')
#plt.ylabel('Precos')
#plt.show() 
#plt.plot(np.arange(1,13,1),moscow_ano1)
#plt.plot(np.arange(1,13,1),moscow_ano2)
#plt.plot(np.arange(1,13,1),moscow_ano3)
#plt.plot(np.arange(1,13,1),moscow_ano4)
#plt.title('Variação do preço maças ano 1 ')
#plt.legend(['Ano 1','Ano 2','Ano 3','Ano 4'])
#plt.xlabel('Meses')
#plt.ylabel('Preco')




























    













    

    
    
        



    







    










    


        
    




















   

























    



                                                                                                             

    










    
    
    
    








    



   
   








    
        

    



    
    
    
    


    
    


