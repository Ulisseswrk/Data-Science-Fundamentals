import numpy as np
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/Marina-Falcao-DEV/apples_ts.csv-Alura-_-Numpy-/refs/heads/main/apples_ts.csv'
dado = np.loadtxt(url,delimiter=',',usecols=np.arange(1,88,1)) #separa os dados por , e comeca da primeira coluna numeral
dado_transposto = dado.T

datas = dado_transposto[:, 0]
precos = dado_transposto[:, 1:6]

moscow = precos[:,0]
kaliningrad = precos[:,1]
petersburg = precos[:,2]
krasnodar = precos[:,3]
ekaterinburg = precos[:,4]

kaliningrad[4] =  np.mean([kaliningrad[3],kaliningrad[5]])
print(kaliningrad)