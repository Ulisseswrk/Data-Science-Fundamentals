#Calculo do índice glicemico com base em valores pré estipulados

glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]
lista = [('Hipoglicemia') if i <= 70 else ('Normal') if 99 > i > 70 else ('Alterada') if 125> i > 100 else ('Diabetes') for i in glicemia]

print(lista)