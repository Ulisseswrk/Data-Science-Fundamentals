estoque = { 
    "Caderno universitario": 50, 
    "Caneta azul": 120, 
    "Borracha branca": 30 
}

produto = input("Digite o nome do produto a ser trocado: ").strip().capitalize()
qntd = int(input("Digite a nova quantidade: "))

if produto in estoque:
    estoque[produto] = qntd
    print(f"Quantidade de '{produto}' atualizada para {qntd}.")

else:
    print(f"Produto '{produto}' não encontrado no estoque.")

print(estoque)