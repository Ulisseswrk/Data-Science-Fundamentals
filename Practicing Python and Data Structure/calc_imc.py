lista_de_tuplas = []
lista_de_imc = []
soma = 0

atletas = [
    ["Maria Silva", 1.75, 65],
    ["João Santos", 1.80, 72],
    ["Ana Pereira", 1.68, 58],
    ["Pedro Oliveira", 1.92, 85],
    ["Carlos Lima", 1.85, 78],
    ["Beatriz Souza", 1.70, 60],
    ["Fernanda Costa", 1.62, 55],
    ["Lucas Almeida", 1.88, 82],
    ["Rafaela Gomes", 1.74, 63],
    ["Gustavo Ferreira", 1.90, 88],
    ["Larissa Rocha", 1.66, 57],
    ["Henrique Nunes", 1.83, 76],
    ["Juliana Martins", 1.72, 59],
    ["Ricardo Carvalho", 1.86, 80],
    ["Sofia Alves", 1.64, 54],
    ["Matheus Ribeiro", 1.89, 84],
    ["Camila Duarte", 1.69, 61],
    ["Gabriel Monteiro", 1.77, 73],
    ["Eduarda Farias", 1.71, 62],
    ["Thiago Mendes", 1.84, 79],
]

for x in atletas:
    nome = x[0]
    altura = x[1]
    peso = x[2]
    alturas = [i[1] for i in atletas]
    lista_de_tuplas.append((nome, altura, peso))
    lista_de_imc.append((nome,imc))

maiores_imc = [i for i in lista_de_imc if i[1] > 23.5]
media_alturas = round(sum(alturas) / len(lista_de_tuplas),2)

print(f'As pessoas com o imc maior que 23.5 são:')
for nome,imc in maiores_imc:
    print(f'{nome}, IMC: {imc}')