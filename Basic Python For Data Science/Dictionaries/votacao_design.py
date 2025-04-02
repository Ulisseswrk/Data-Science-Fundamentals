mais_votado = 0
design_favorito = 0

votos = {'Design 1': 1334,'Design 2': 982,'Design 3':  1751,'Design 4': 210,'Design 5': 1811, }

for voto in votos.keys():
    if mais_votado < votos[voto]:
        mais_votado = votos[voto]
        design_favorito = voto

porcentagem = (mais_votado / sum(votos.values()) * 100)

print(f"\nDentre as opções:\n{", ".join(votos.keys())}", end = ".")

print(f"\n\nO mais votado foi: {design_favorito} com {mais_votado}\nRepresentando assim: {round(porcentagem,2)}% dos votos.")


