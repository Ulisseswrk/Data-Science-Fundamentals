import numpy as np #importei a biblioteca numpy como np
import matplotlib.pyplot as plt #importei a biblioteca matplotlib como plt

#Atrelei a url a uma variavel para cita-la na criação do array
url = 'https://raw.githubusercontent.com/Marina-Falcao-DEV/apples_ts.csv-Alura-_-Numpy-/refs/heads/main/apples_ts.csv' 

#Loadtxt carrega um arquivo, delimiter seta o espaçamento for i in arquivo e usecols define as colunas, e no arange a gente seleciona somente a segunda (indice 1)
dado = np.loadtxt(url,delimiter=',',usecols=np.arange(1,88,1)) 

#Utiliza o método T para transpor o dado, ou seja oq era coluna agora vira linha e etc
dado_transposto = dado.T #

#Pega todo o intervalo de linhas anteriores com o : e separa as linhas das colunas com virgula
datas = dado_transposto[:, 0] 
precos = dado_transposto[:, 1:6]

#Dessa linha pra baixo começa o exercicio, e para ele, foi pedido o diametro e peso da laranja e da toranja

#Os dados da laranja ficavam da linha 0 até a 4999 e na coluna um
diametro_laranja = dado[:5000,0]
peso_laranja = dado[:5000,0]

#Enquanto os da tonranja ficavam da 5000 em diante
peso_toranja = dado[5000:,1]
diametro_toranja = dado[5000:,1]

plt.plot(peso_laranja,diametro_laranja)
plt.plot(peso_toranja,diametro_toranja)
plt.show()