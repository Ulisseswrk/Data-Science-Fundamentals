laura = input('Digite os itens da lista da laura: ').lower().split(' ')
ana = input('Digite os itens da lista da ana: ').lower().split(' ')

repetidos = [i for i in laura if i in ana]

exclusivo_laura = [i for i in laura if i not in ana]
exclusivo_ana = [i for i in ana if i not in laura]

print(f'\nItens em ambas as Listas: {', '.join(repetidos)}')
print(f'Itens exclusivos de Laura: {', '.join(exclusivo_laura)}')
print(f'Itens exclusivos de Ana: {', '.join(exclusivo_ana)}')