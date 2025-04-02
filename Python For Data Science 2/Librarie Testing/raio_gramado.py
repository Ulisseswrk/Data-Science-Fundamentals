from math import pi, pow

raio = float(input('Digite o raio da área circular: '))

area = pi * pow(raio,2)

print(f'\nO metro quadrado do nosso gramado custa R$ 25,00\n'
      f'Logo, pela como sua area é {round(area,2)} m², o valor final é: R$ {round(25 * area,2)}')