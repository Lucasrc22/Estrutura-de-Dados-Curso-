class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
    
    def mostra_no(self):
        print(self.valor)

class ListaEncadeada:
    def __init__(self):
        self.primeiro = None
    
    def lista_vazia(self):
        return self.primeiro is None

    def insere_inicio(self, valor):
        novo = No(valor)
        novo.proximo = self.primeiro
        self.primeiro = novo

    def excluir_inicio(self):
        if self.lista_vazia():
            print("Lista está vazia")
            return None
        temp = self.primeiro
        self.primeiro = self.primeiro.proximo
        return temp

class PilhaListaEncadeada:
    def __init__(self):
        self.lista = ListaEncadeada()
    
    def empilhar(self, valor):
        self.lista.insere_inicio(valor)
    
    def desempilhar(self):
        no_removido = self.lista.excluir_inicio()
        if no_removido:
            return no_removido.valor
        return None

    def pilha_vazia(self):
        return self.lista.lista_vazia()
    
    def ver_topo(self):
        if self.lista.lista_vazia():
            print("Pilha está vazia")
            return None
        return self.lista.primeiro.valor

# Testando a classe PilhaListaEncadeada
pilha = PilhaListaEncadeada()

# Empilhando elementos
pilha.empilhar(10)
pilha.empilhar(20)
pilha.empilhar(30)
pilha.empilhar(40)

# Visualizando o topo da pilha
print("Topo da pilha:", pilha.ver_topo())  # Deve imprimir 40

# Desempilhando um elemento
print("Desempilhando:", pilha.desempilhar())

# Visualizando o topo da pilha após desempilhar
print("Topo da pilha após desempilhar:", pilha.ver_topo())  # Deve imprimir 30

# Desempilhando todos os elementos
print("\nDesempilhando todos os elementos:")
while True:
    topo_atual = pilha.ver_topo()
    if topo_atual is None:
        break
    print("Elemento no topo:", topo_atual)
    pilha.desempilhar()
