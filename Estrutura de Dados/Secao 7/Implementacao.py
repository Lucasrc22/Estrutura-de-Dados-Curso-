class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None

    def mostra_no(self):
        print(self.valor)

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def __lista_vazia(self):
        return self.primeiro is None

    def insere_inicio(self, valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.ultimo = novo
        else:
            self.primeiro.anterior = novo
        novo.proximo = self.primeiro
        self.primeiro = novo

    def insere_final(self, valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.primeiro = novo
        else:
            self.ultimo.proximo = novo
            novo.anterior = self.ultimo
        self.ultimo = novo

    def excluir_inicio(self):
        if self.__lista_vazia():
            print("A lista está vazia")
            return None
        temp = self.primeiro
        if self.primeiro == self.ultimo:  # Caso tenha apenas um elemento
            self.primeiro = self.ultimo = None
        else:
            self.primeiro = self.primeiro.proximo
            self.primeiro.anterior = None
        return temp

    def excluir_final(self):
        if self.__lista_vazia():
            print("A lista está vazia")
            return None
        temp = self.ultimo
        if self.primeiro == self.ultimo:  # Caso tenha apenas um elemento
            self.primeiro = self.ultimo = None
        else:
            self.ultimo = self.ultimo.anterior
            self.ultimo.proximo = None
        return temp

    def excluir_posicao(self, valor):
        if self.__lista_vazia():
            print("A lista está vazia")
            return None
        atual = self.primeiro
        while atual is not None and atual.valor != valor:
            atual = atual.proximo
        if atual is None:  # Valor não encontrado
            print(f"Valor {valor} não encontrado na lista.")
            return None
        if atual == self.primeiro:  # Caso o valor esteja no primeiro nó
            return self.excluir_inicio()
        if atual == self.ultimo:  # Caso o valor esteja no último nó
            return self.excluir_final()
        # Caso o valor esteja em outro nó
        atual.anterior.proximo = atual.proximo
        atual.proximo.anterior = atual.anterior
        return atual

    def mostrar_frente(self):
        if self.__lista_vazia():
            print("A lista está vazia")
            return
        atual = self.primeiro
        while atual is not None:
            atual.mostra_no()
            atual = atual.proximo

    def mostrar_tras(self):
        if self.__lista_vazia():
            print("A lista está vazia")
            return
        atual = self.ultimo
        while atual is not None:
            atual.mostra_no()
            atual = atual.anterior


# Teste do código
print("Testando Lista Duplamente Encadeada")
lista = ListaDuplamenteEncadeada()

# Inserindo no início
print("\nInserindo no início:")
lista.insere_inicio(10)
lista.insere_inicio(20)
lista.insere_inicio(30)
lista.mostrar_frente()

# Inserindo no final
print("\nInserindo no final:")
lista.insere_final(40)
lista.insere_final(50)
lista.mostrar_frente()

# Excluindo do início
print("\nExcluindo do início:")
excluido = lista.excluir_inicio()
print(f"Excluído: {excluido.valor}")
lista.mostrar_frente()

# Excluindo do final
print("\nExcluindo do final:")
excluido = lista.excluir_final()
print(f"Excluído: {excluido.valor}")
lista.mostrar_frente()

# Excluindo por valor
print("\nExcluindo valor 20:")
excluido = lista.excluir_posicao(20)
if excluido:
    print(f"Excluído: {excluido.valor}")
lista.mostrar_frente()
