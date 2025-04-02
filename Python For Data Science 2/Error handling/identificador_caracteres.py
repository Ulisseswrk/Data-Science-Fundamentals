def removedor(lista:list) -> list:
    for i in lista:
        if ":" in i or ";" in i:
            return i
    return ""

frase = "A tecnologia evolui: rapidamente; transformando o mundo ao nosso redor."
lista_palavras = frase.split()

frase_corrigida = removedor(lista_palavras).replace(":","").replace(";","")

try:
    if ":" in removedor(lista_palavras) or ";" in removedor(lista_palavras):
        raise ValueError("A frase não pode conter caracteres especiais")
except ValueError as e:
    print(f"Caracteres especiais foram usados após a palavra {frase_corrigida}. {e}")
else:
    print("A palavra não tem caracteres especiais")
finally:
    print("Fim do código")