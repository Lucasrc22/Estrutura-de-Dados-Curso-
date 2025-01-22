class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
    
    def mostrar_no(self):
        print(self.valor)


class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None
        self.ligacoes = []

    def inserir(self, valor):
        novo = No(valor)
        if self.raiz is None:
            self.raiz = novo
        else:
            atual = self.raiz
            while True:
                pai = atual
                if valor < atual.valor:  # Esquerda
                    atual = atual.esquerda
                    if atual is None:
                        pai.esquerda = novo
                        self.ligacoes.append(f"{pai.valor} -> {novo.valor}")
                        return
                else:  # Direita
                    atual = atual.direita
                    if atual is None:
                        pai.direita = novo
                        self.ligacoes.append(f"{pai.valor} -> {novo.valor}")
                        return

    def pesquisar(self, valor):
        atual = self.raiz
        while atual is not None:
            if valor == atual.valor:
                return atual
            elif valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita
        return None

    # Pré-ordem (raiz, esquerda, direita)
    def pre_ordem(self, no):
        if no is not None:
            print(no.valor)
            self.pre_ordem(no.esquerda)
            self.pre_ordem(no.direita)

    # Em ordem (esquerda, raiz, direita)
    def em_ordem(self, no):
        if no is not None:
            self.em_ordem(no.esquerda)
            print(no.valor)
            self.em_ordem(no.direita)

    # Pós-ordem (esquerda, direita, raiz)
    def pos_ordem(self, no):
        if no is not None:
            self.pos_ordem(no.esquerda)
            self.pos_ordem(no.direita)
            print(no.valor)

    def excluir(self, valor):
        if self.raiz is None:
            print("A árvore está vazia")
            return False

        atual = self.raiz
        pai = None
        e_esquerda = True

        # Localizar o nó a ser removido
        while atual is not None and atual.valor != valor:
            pai = atual
            if valor < atual.valor:
                e_esquerda = True
                atual = atual.esquerda
            else:
                e_esquerda = False
                atual = atual.direita

        if atual is None:  # Nó não encontrado
            return False

        # Caso 1: Nó é uma folha
        if atual.esquerda is None and atual.direita is None:
            if atual == self.raiz:
                self.raiz = None
            elif e_esquerda:
                pai.esquerda = None
            else:
                pai.direita = None

        # Caso 2: Nó tem apenas um filho (esquerda)
        elif atual.direita is None:
            if atual == self.raiz:
                self.raiz = atual.esquerda
            elif e_esquerda:
                pai.esquerda = atual.esquerda
            else:
                pai.direita = atual.esquerda

        # Caso 2: Nó tem apenas um filho (direita)
        elif atual.esquerda is None:
            if atual == self.raiz:
                self.raiz = atual.direita
            elif e_esquerda:
                pai.esquerda = atual.direita
            else:
                pai.direita = atual.direita

        # Caso 3: Nó tem dois filhos
        else:
            sucessor = self.get_sucessor(atual)
            if atual == self.raiz:
                self.raiz = sucessor
            elif e_esquerda:
                pai.esquerda = sucessor
            else:
                pai.direita = sucessor
            sucessor.esquerda = atual.esquerda

        return True

    def get_sucessor(self, no):
        pai_sucessor = no
        sucessor = no
        atual = no.direita
        while atual is not None:
            pai_sucessor = sucessor
            sucessor = atual
            atual = atual.esquerda

        if sucessor != no.direita:
            pai_sucessor.esquerda = sucessor.direita
            sucessor.direita = no.direita

        return sucessor


# Testando a árvore
arvore = ArvoreBinariaBusca()

# Inserindo valores na árvore
valores = [53, 54, 23, 87, 98, 22, 12, 11, 10]
for valor in valores:
    arvore.inserir(valor)

# Excluindo um nó
arvore.excluir(10)

# Testes de impressão
print("Ligações após exclusão:")
for ligacao in arvore.ligacoes:
    print(ligacao)

# Pesquisando elementos
pesquisa_valores = [87, 23, 99]  # Incluindo um valor que não existe
for valor in pesquisa_valores:
    resultado = arvore.pesquisar(valor)
    if resultado:
        print(f"Valor {valor} encontrado na árvore.")
    else:
        print(f"Valor {valor} NÃO encontrado na árvore.")

# Testes de percurso
print("\nPercurso Pré-Ordem:")
arvore.pre_ordem(arvore.raiz)

print("\nPercurso Em-Ordem:")
arvore.em_ordem(arvore.raiz)

print("\nPercurso Pós-Ordem:")
arvore.pos_ordem(arvore.raiz)

# Inserindo mais valores para verificar atualização
novos_valores = [100, 5, 75]
for valor in novos_valores:
    arvore.inserir(valor)

print("\nLigações após inserir novos valores:")
for ligacao in arvore.ligacoes:
    print(ligacao)

# Excluindo mais valores
excluir_valores = [23, 12]
for valor in excluir_valores:
    arvore.excluir(valor)

print("\nLigações após excluir valores adicionais:")
for ligacao in arvore.ligacoes:
    print(ligacao)

