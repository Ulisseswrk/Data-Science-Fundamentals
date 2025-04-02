#Criaçao de lista invertida com as palavras cujo numero de letras é par

palavras = ["banana", "abacate", "python", "exercicios", "algoritmo", "lista"]

lista_invertida = [i[::-1] for i in palavras if len(i) % 2 == 0]
print(lista_invertida)