cidades = ("SALVADOR","FORTALEZA","NATAL","ARACAJU")
valor_passeios = [200, 400, 250, 300]
distancias = [200, 400, 250, 300]

diaria = 150
consumo = 14
gasolina = 5

dias = float(input("Digite o tempo de estadia: "))

def gasto_hotel(diaria: float,dias: int) -> float:
    return diaria * dias

def gasto_gasolina(cidade:str, distancias:list ,consumo:float, gasolina:float) -> float:
    for i in range(len(distancias)):

        if cidade == "SALVADOR": # É Salvador
            return ((distancias[0] / consumo) * gasolina)
        elif cidade == "FORTALEZA": # É Fortaleza
            return ((distancias[1] / consumo) * gasolina)
        elif cidade == "NATAL": # É Natal
            return ((distancias[2] / consumo) * gasolina)
        elif cidade == "ARACAJU": # É Aracaju
            return ((distancias[3] / consumo) * gasolina)
        
def gasto_passeio(valor_passeios:list) -> float:
    
    for i in valor_passeios:

        if i == valor_passeios[0]:
            return valor_passeios[0] 
        
        elif i == valor_passeios[1]:
            return valor_passeios[1] 
        
        elif i == valor_passeios[2]:
            return valor_passeios[2]
        
        elif i == valor_passeios[3]:
            return valor_passeios[3]

while True: 
    cidade = input("Digite sua cidade desejada: ").upper()

    if cidade not in cidades:
        cidade = input("Cidade inválida, digite novamente: ").upper()

    else:
        break

gasto_total = gasto_hotel(diaria) + gasto_gasolina(cidade, distancias,consumo,gasolina) + gasto_passeio(valor_passeios) * dias

print(f"O valor da viajar para {cidade.capitalize()} é {round(gasto_total,2)}")