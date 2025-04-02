contador = 0

while True:
    meses = ("JANEIRO","FEVEREIRO","MARCO","ABRIL","MAIO","JUNHO","JULHO","AGOSTO","SETEMBRO","OUTUBRO","NOVEMBRO","DEZEMBRO")
    meses_30_dias = ["ABRIL", "JUNHO", "SETEMBRO", "NOVEMBRO"]

    dia = int(input("Informe um dia: ").strip())
    mes = input("Informe um mês: ").strip().upper()
    ano = int(input("Informe um ano: ").strip())
    contador += 1
    
    if contador == 3:
        sair = input("Digite S/N para sair").strip().upper()
        if sair == "SIM":
            break
            
    if contador == 1:
        print("")

    if dia < 1 or dia > 31:
        print("Dia inválido")
        continue

    if ano > 2025:
        print("Ano inválido")
        continue

    if mes in meses[2:11] and dia > 13 and ano == 2025:
        print("Essa data ainda não chegou")
        continue

    if mes not in meses:
        print("Esse mes não existe")
        continue

    if mes in meses_30_dias and dia > 30:
        print("Esse mes não tem 31 dias, tente novamente:\n")
        continue

    if mes == "FEVEREIRO" and dia == 29:
        if (ano % 4 != 0) and (ano % 100 == 0 and ano % 400 != 0):
            print("O ano não é bissexto, logo fevereiro não tem 29 dias")
            continue

    else:
        print("Obrigado por colaborar, fim do código.")
    break
