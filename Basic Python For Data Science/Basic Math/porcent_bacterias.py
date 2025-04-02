bacterias = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]

crescimentos = []

for i in range(1,len(bacterias)):

    crescimento =  round(100 * (bacterias[i] - bacterias[i-1]) / (bacterias[i-1]), 2)
    crescimentos.append(crescimento)
    
print(f"O crecimento por dia de {crescimentos}")