class No:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    
    def ShowNo(self):
        print(self.value, end=" ")

class Cliente:
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return f"Cliente {self.value}"

class Caixa:
    def __init__(self):
        self.fila = []
    
    def is_empty(self):
        return len(self.fila) == 0

    def novo_cliente(self, cliente):
        self.fila.append(cliente)
        print(f"{cliente} entrou na fila.")

    def atender_cliente(self):
        if self.is_empty():
            print("Não há clientes na fila.")
            return None
        cliente_atendido = self.fila.pop(0)
        print(f"{cliente_atendido} foi atendido.")
        return cliente_atendido
    
    def mostrar_fila(self):
        if self.is_empty():
            print("Fila vazia.")
        else:
            print("Fila atual:", [str(cliente) for cliente in self.fila])

class Loja:
    def __init__(self):
        self.caixas = [Caixa() for _ in range(3)]
    
    def abre_caixa(self):
        self.caixas.append(Caixa())
        print(f"Novo caixa aberto. Total de caixas: {len(self.caixas)}")

    def novo_cliente(self, cliente):
        caixa_menor_fila = min(self.caixas, key=lambda x: len(x.fila))
        caixa_menor_fila.novo_cliente(cliente)

    def atende_cliente(self, i):
        if 0 <= i < len(self.caixas):
            self.caixas[i].atender_cliente()
        else:
            print("Caixa inválido.")

    def fechar_caixas(self):
        self.caixas = []
        print("Todos os caixas foram fechados.")

    def parar_caixa(self, i):
        if 0 <= i < len(self.caixas):
            del self.caixas[i]
            print(f"Caixa {i} foi fechado. Caixas restantes: {len(self.caixas)}")
        else:
            print("Caixa inválido.")

    def mostrar_filas(self):
        for i, caixa in enumerate(self.caixas):
            print(f"Caixa {i}: ", end="")
            caixa.mostrar_fila()

loja = Loja()
loja.novo_cliente(Cliente(1))
loja.novo_cliente(Cliente(2))
loja.novo_cliente(Cliente(3))
loja.mostrar_filas()
print()
loja.atende_cliente(0)
loja.mostrar_filas()
print()
loja.abre_caixa()
loja.novo_cliente(Cliente(4))
loja.mostrar_filas()
print()
loja.parar_caixa(1)
loja.mostrar_filas()
loja.fechar_caixas()
