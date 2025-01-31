import numpy as np

# Dicionário de vértices (cidade -> índice)
vertices = {'arad': 0, 'zerind': 1, 'oradea': 2, 'sibiu': 3, 'timisoara': 4,
            'lugoj': 5, 'mehadia': 6, 'dobreta': 7, 'craiova': 8, 'rimnicu': 9,
            'fagaras': 10, 'pitesti': 11, 'bucharest': 12, 'giurgiu': 13}

# Dicionário reverso (índice -> cidade)
cidades = {v: k for k, v in vertices.items()}

# Inicializa a matriz de adjacência com zeros
arestas = np.zeros((len(vertices), len(vertices)), dtype=int)

# Definição das conexões e distâncias entre as cidades
conexoes = [
    ('arad', 'zerind', 75), ('arad', 'sibiu', 140), ('arad', 'timisoara', 118),
    ('zerind', 'oradea', 71), ('oradea', 'sibiu', 151), ('sibiu', 'fagaras', 99),
    ('sibiu', 'rimnicu', 80), ('timisoara', 'lugoj', 111), ('lugoj', 'mehadia', 70),
    ('mehadia', 'dobreta', 75), ('dobreta', 'craiova', 120), ('craiova', 'pitesti', 138),
    ('craiova', 'rimnicu', 146), ('rimnicu', 'pitesti', 97), ('fagaras', 'bucharest', 211),
    ('pitesti', 'bucharest', 101), ('bucharest', 'giurgiu', 90)
]

# Preenchendo a matriz de adjacência
for cidade1, cidade2, distancia in conexoes:
    i, j = vertices[cidade1], vertices[cidade2]
    arestas[i, j] = distancia
    arestas[j, i] = distancia  # Grafo não-direcionado

# Exibir matriz com os nomes das cidades
print("\nMatriz de adjacência (distâncias entre cidades):\n")
print("     " + "  ".join(f"{cidades[i][:6]:>6}" for i in range(len(cidades))))  # Cabeçalho
print("   " + "-" * (len(cidades) * 8))

for i in range(len(arestas)):
    linha = "  ".join(f"{arestas[i, j]:>6}" for j in range(len(arestas)))  # Formata os valores
    print(f"{cidades[i][:6]:>6} | {linha}")  # Nome da cidade + valores da linha
