class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def mostra_no(self):
        print(self.valor)


class ListaEncadeadaExtremidadeDupla:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def lista_vazia(self):
        return self.primeiro is None

    def insere_final(self, valor):
        novo = No(valor)
        if self.lista_vazia():
            self.primeiro = novo
        else:
            self.ultimo.proximo = novo
        self.ultimo = novo

    def excluir_inicio(self):
        if self.lista_vazia():
            print("Lista está vazia")
            return None

        temp = self.primeiro
        if self.primeiro.proximo is None:
            self.ultimo = None
        self.primeiro = self.primeiro.proximo
        return temp


class FilaListaEncadeada:
    def __init__(self):
        self.lista = ListaEncadeadaExtremidadeDupla()

    def fila_vazia(self):
        return self.lista.lista_vazia()

    def enfileirar(self, valor):
        self.lista.insere_final(valor)

    def desenfileirar(self):
        no_removido = self.lista.excluir_inicio()
        if no_removido:
            return no_removido.valor
        return None

    def ver_inicio(self):
        if self.lista.lista_vazia():
            print("Fila está vazia")
            return None
        return self.lista.primeiro.valor


# Testando a classe FilaListaEncadeada
fila = FilaListaEncadeada()

# Enfileirando elementos
fila.enfileirar(10)
fila.enfileirar(20)
fila.enfileirar(30)

# Verificando o início da fila
print("Início da fila:", fila.ver_inicio())  # Deve imprimir 10

# Desenfileirando elementos
print("Desenfileirado:", fila.desenfileirar())  # Deve imprimir 10
print("Início da fila após desenfileirar:", fila.ver_inicio())  # Deve imprimir 20

# Desenfileirando mais elementos
print("Desenfileirado:", fila.desenfileirar())  # Deve imprimir 20
print("Desenfileirado:", fila.desenfileirar())  # Deve imprimir 30

# Tentando desenfileirar de uma fila vazia
print("Desenfileirado de uma fila vazia:", fila.desenfileirar())  # Deve imprimir None

# Verificando se a fila está vazia
print("A fila está vazia?", fila.fila_vazia())  # Deve imprimir True
