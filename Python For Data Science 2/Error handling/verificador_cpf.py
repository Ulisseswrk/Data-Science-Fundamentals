cpf_verificado = []

try: #Mecanismo de tentativa de um determinado código
    cpf = input('Digite seu CPF: ')
    cpf = cpf.replace('-','').replace('.','')
    
    if not cpf.isdigit(): # verifica se existe alguma letra em CPF
        raise ValueError('Erro: CPF deve conter apenas números ❌')

    if len(cpf) != 11:
        print('CPF inválido, não tem 11 números ❌')
    
    cpf = [int(i) for i in cpf]
    
except ValueError: #Caso dê ValueError, printar a mensagem
    while True:
        cpf = input('Digite seu CPF corretamente (somente 11 números): ')

        if cpf.isdigit() and len(cpf) == 11:
            cpf = [int(i) for i in cpf]
            cpf = cpf.replace('-', '').replace('.', '')
            break
        
finally:
    cpf_verificado = cpf[:9]

#Verificação do primeiro digito verificador:
    soma = 0
    contador = 10

    for i in range(9):
        soma += cpf_verificado[i] * contador
        contador -= 1

    digito1 = 11 - (soma % 11)
    if digito1 >= 10:
        digito1 = 0

    cpf_verificado.append(digito1)

#Verificação do segundo digito verificador:
    soma = 0
    contador = 11

    for i in range(10):
        soma += cpf_verificado[i] * contador
        contador -= 1

    digito2 = 11 - (soma % 11) # calc 2 digito 2

    if digito2 >= 10:
        digito2 = 0

    cpf_verificado.append(digito2)


    if cpf == cpf_verificado:
        print('CPF verídico ✅')
    else:
        print('CPF inválido ❌')
        
#Só a título de curiosidade, essa foi a primeira versão do código:

# cpf = input('Digite seu CPF: ')
# cpf = [int(i) for i in cpf]
# cpf_verificado = []

# contador = 0

# #Verificação do primeiro digito verificador:

# while len(cpf_verificado) != 9: #Loop pra coletar apenas os 9 primeiros números digitados
#     cpf_verificado.append(cpf[contador])
#     contador += 1

# for i in 
# c1_d1 = cpf[0] * 10 + cpf[1] * 9 + cpf[2] * 8 + cpf[3] * 7 + cpf[4] * 6 + cpf[5] * 5 + cpf[6] * 4 + cpf[7] * 3 + cpf[8] * 2 #calc 1 digito 1
# c2_d1 = 11 - (c1_d1 % 11) #calc 2 digito 1

# cpf_verificado.append(c2_d1) #Adicionando o resultado pra lista

# c1_d2 = cpf[0] * 11 + cpf[1] * 10 + cpf[2] * 9 + cpf[3] * 8 + cpf[4] * 7 + cpf[5] * 6 + cpf[6] * 5 + cpf[7] * 4 + cpf[8] * 3 + cpf[9] * 2 #calc 1 digito 2
# c2_d2 = 11 - (c1_d2 % 11) # calc 2 digito 2

# cpf_verificado.append(c2_d2)

# print(cpf)
# print(cpf_verificado)
