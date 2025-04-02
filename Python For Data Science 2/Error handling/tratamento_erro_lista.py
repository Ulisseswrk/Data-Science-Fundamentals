def agrupador(l1,l2:list) -> list:

    try:
        dados = [(l1[i], l2[i], l1[i]+l2[i]) for i in range(len(l1))]
    except IndexError:
        print('Uma das listas é maior que a outra') #In case of one of the list being bigger than the other
    except TypeError:
        print('A lista só pode ter números') #If someone inserting a string at the list
    except NameError:
        print('A não pode ter variaveis') #In case of someone inserting an a at the list without the '' for example
    else:
        return dados
    finally: 
        return 'Fim do Programa' #The end of the function

lista1 = [1,2,3,4,5,6,7,8,9,10,]
lista2 = [6,5,7,3,5,4,7,6,8,70]

print(agrupador(lista1,lista2))