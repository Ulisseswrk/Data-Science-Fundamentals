def avaliador(x):
    x.remove(max(x))
    x.remove(min(x))
    
    return sum(x) / len(x)

notas = []

for i in range(1,6):
    nota = float(input('Digite a nota do skatista: '))
    notas.append(nota)

print(f'A pontuação do skatista foi: {avaliador(notas)}')