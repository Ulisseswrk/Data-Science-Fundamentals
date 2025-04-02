nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]

identificadora = map(lambda x, y: f"{x.capitalize()} {y.capitalize()}", nomes, sobrenomes)

for i in identificadora:
    print(f"Nome completo: {i}")