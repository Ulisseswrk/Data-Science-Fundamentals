from random import choice

contador = 0
frutas = ["maçã", "banana", "uva", "pêra", 
          "manga", "coco", "melancia", "mamão",
          "laranja", "abacaxi", "kiwi", "ameixa"]

for i in frutas:
    if contador == 0:
        print('Sua salada de frutas será composta por:', end = ' ')

    print(f'{choice(frutas)}', end = ', ')
    contador += 1

    if contador == 2:
        print(choice(frutas), end = '. ')
        break