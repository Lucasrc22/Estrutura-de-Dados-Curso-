def eh_arvore_binaria(arestas):
    filhos = {}
    todos_os_nos = []
    pais = []

    for pai, filho in arestas:
        if pai not in filhos:
            filhos[pai] = []
        filhos[pai].append(filho)
        if len(filhos[pai]) > 2:
            return False
        if filho in pais:
            return False
        pais.append(filho)
        if pai not in todos_os_nos:
            todos_os_nos.append(pai)
        if filho not in todos_os_nos:
            todos_os_nos.append(filho)

    raiz = None
    for no in todos_os_nos:
        if no not in pais:
            if raiz is None:
                raiz = no
            else:
                return False
    if raiz is None:
        return False

    visitados = []
    fila = [raiz]

    while fila:
        atual = fila.pop(0)
        if atual in visitados:
            return False
        visitados.append(atual)
        if atual in filhos:
            for f in filhos[atual]:
                fila.append(f)

    return len(visitados) == len(todos_os_nos)

arestas = []

while True:
    entrada = input()
    if entrada.strip().lower() == "fim":
        break
    try:
        pai, filho = map(int, entrada.split())
        arestas.append((pai, filho))
    except:
        print("Entrada inválida")

if eh_arvore_binaria(arestas):
    print("Parece uma árvore binária!")
else:
    print("Isso não é uma árvore binária!")
