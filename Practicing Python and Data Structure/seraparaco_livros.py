livros = [
    ("Dom Quixote", "Miguel de Cervantes", 1605),
    ("Orgulho e Preconceito", "Jane Austen", 1813),
    ("O Grande Gatsby", "F. Scott Fitzgerald", 1925),
    ("Cem Anos de Solidão", "Gabriel García Márquez", 1967),
    ("1984", "George Orwell", 1949),
    ("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997),
    ("O Senhor dos Anéis", "J.R.R. Tolkien", 1954),
    ("A Revolução dos Bichos", "George Orwell", 1945),
    ("O Apanhador no Campo de Centeio", "J.D. Salinger", 1951),
    ("O Código Da Vinci", "Dan Brown", 2003),
]

autor = {}
catalogo = {i[0]: {"autor":i[1], "ano":i[2]}
    for i in livros}

livros_antigos = {titulo:info 
    for titulo,info in catalogo.items() 
    if info["ano"] < 1950}

print(livros_antigos)

#--------------------------------------------------------------------------------------------------------

#Acrescimo de um dict comprehension que diz quantos anos tem cada livro

# catalogo = {
#     "Dom Quixote": {"autor": "Miguel de Cervantes", "ano": 1605},
#     "Orgulho e Preconceito": {"autor": "Jane Austen", "ano": 1813},
#     "O Grande Gatsby": {"autor": "F. Scott Fitzgerald", "ano": 1925},
#     "Cem Anos de Solidão": {"autor": "Gabriel García Márquez", "ano": 1967},
#     "1984": {"autor": "George Orwell", "ano": 1949},
#     "Harry Potter e a Pedra Filosofal": {"autor": "J.K. Rowling", "ano": 1997},
#     "O Senhor dos Anéis": {"autor": "J.R.R. Tolkien", "ano": 1954},
#     "A Revolução dos Bichos": {"autor": "George Orwell", "ano": 1945},
#     "O Apanhador no Campo de Centeio": {"autor": "J.D. Salinger", "ano": 1951},
#     "O Código Da Vinci": {"autor": "Dan Brown", "ano": 2003},
# }

# livros_atualizados = {autor: 2025 - info["ano"] for autor,info in catalogo.items()}

# for x, y in livros_atualizados.items():
#     print(f"{x} tem {y} anos")