# Definição da classe "No" que representará cada nó da lista
class No:
    def __init__(self, valor):
        self.valor = valor  # Valor armazenado no nó
        self.proximo = None  # Ponteiro para o próximo nó (utilizado na lista encadeada simples)
        self.anterior = None  # Ponteiro para o nó anterior (utilizado na lista encadeada de extremidade dupla)

    def mostrar_no(self):
        print(self.valor)  # Exibe o valor do nó

# Definição da classe "ListaEncadeada" (Lista Encadeada Simples)
class ListaEncadeada:
    def __init__(self):
        self.primeiro = None  # Inicializa a lista vazia (sem elementos)

    def insereInicio(self, valor):
        novo = No(valor)  # Cria um novo nó com o valor passado
        novo.proximo = self.primeiro  # O novo nó aponta para o primeiro nó atual
        self.primeiro = novo  # O novo nó se torna o primeiro nó da lista

    def mostrar(self):
        if self.primeiro is None:
            print("A lista está vazia")  # Se a lista estiver vazia, imprime mensagem
            return

        atual = self.primeiro  # Começa do primeiro nó
        while atual is not None:  # Continua até o final da lista
            atual.mostrar_no()  # Exibe o valor do nó atual
            atual = atual.proximo  # Avança para o próximo nó

    def pesquisa(self, valor):
        if self.primeiro is None:
            print("A lista está vazia")  # Se a lista estiver vazia, exibe mensagem
            return None

        atual = self.primeiro  # Começa do primeiro nó
        while atual is not None:  # Continua até o final da lista
            if atual.valor == valor:  # Se encontrar o valor no nó atual
                return atual  # Retorna o nó que contém o valor
            atual = atual.proximo  # Avança para o próximo nó
        
        print(f"Valor {valor} não encontrado na lista.")  # Se o valor não for encontrado
        return None

    def excluir_inicio(self):
        if self.primeiro is None:
            print("A lista está vazia")  # Se a lista estiver vazia, exibe mensagem
            return None
        
        temp = self.primeiro  # Salva o nó que será excluído
        self.primeiro = self.primeiro.proximo  # O próximo nó se torna o primeiro
        return temp  # Retorna o nó excluído

    def excluir_posicao(self, valor):
        if self.primeiro is None:
            print("A lista está vazia")  # Se a lista estiver vazia, exibe mensagem
            return None
        
        atual = self.primeiro  # Começa do primeiro nó
        anterior = None  # Inicializa o nó anterior como None (será utilizado para linkar nós)
        
        # Procura pelo valor a ser excluído na lista
        while atual is not None and atual.valor != valor:
            anterior = atual  # Atualiza o nó anterior
            atual = atual.proximo  # Avança para o próximo nó
        
        if atual is None:  # Se o valor não for encontrado
            print(f"Valor {valor} não encontrado na lista.")
            return None
        
        if atual == self.primeiro:  # Se o nó a ser excluído é o primeiro
            self.primeiro = self.primeiro.proximo
        else:  # Se o nó a ser excluído não é o primeiro
            anterior.proximo = atual.proximo  # O nó anterior aponta para o próximo do nó atual
        
        return atual  # Retorna o nó excluído

# Definição da classe "ListaEncadeadaExtremidadeDupla" (Lista Encadeada de Extremidade Dupla)
class ListaEncadeadaExtremidadeDupla:
    def __init__(self):
        self.primeiro = None  # Inicializa a lista vazia (sem elementos)
        self.ultimo = None  # Inicializa o último nó como None

    def __lista_vazia(self):
        return self.primeiro is None  # Verifica se a lista está vazia

    def insere_inicio(self, valor):
        novo = No(valor)  # Cria um novo nó com o valor
        if self.__lista_vazia():  # Se a lista estiver vazia
            self.primeiro = self.ultimo = novo  # O novo nó é o primeiro e o último
        else:
            novo.proximo = self.primeiro  # O novo nó aponta para o primeiro nó da lista
            self.primeiro.anterior = novo  # O primeiro nó aponta para o novo nó como anterior
            self.primeiro = novo  # O novo nó se torna o primeiro nó da lista

    def insere_final(self, valor):
        novo = No(valor)  # Cria um novo nó com o valor
        if self.__lista_vazia():  # Se a lista estiver vazia
            self.primeiro = self.ultimo = novo  # O novo nó é o primeiro e o último
        else:
            self.ultimo.proximo = novo  # O último nó aponta para o novo nó
            novo.anterior = self.ultimo  # O novo nó aponta para o último nó como anterior
            self.ultimo = novo  # O novo nó se torna o último nó da lista

    def excluir_inicio(self):
        if self.__lista_vazia():  # Se a lista estiver vazia
            print("A lista está vazia")
            return None
        
        temp = self.primeiro  # Salva o nó que será excluído
        if self.primeiro.proximo is None:  # Se houver apenas um nó
            self.primeiro = self.ultimo = None  # Ambos os ponteiros se tornam None
        else:
            self.primeiro = self.primeiro.proximo  # O próximo nó se torna o primeiro
            self.primeiro.anterior = None  # O novo primeiro nó não aponta para nenhum nó anterior
        return temp  # Retorna o nó excluído

    def excluir_final(self):
        if self.__lista_vazia():  # Se a lista estiver vazia
            print("A lista está vazia")
            return None
        
        temp = self.ultimo  # Salva o nó que será excluído
        if self.primeiro == self.ultimo:  # Se houver apenas um nó
            self.primeiro = self.ultimo = None  # Ambos os ponteiros se tornam None
        else:
            self.ultimo = self.ultimo.anterior  # O nó anterior ao último se torna o último
            self.ultimo.proximo = None  # O novo último nó não aponta para nenhum nó posterior
        return temp  # Retorna o nó excluído

    def mostrar(self):
        if self.__lista_vazia():  # Se a lista estiver vazia
            print("A lista está vazia")
            return
        
        atual = self.primeiro  # Começa do primeiro nó
        while atual:  # Continua até o final da lista
            atual.mostrar_no()  # Exibe o valor do nó atual
            atual = atual.proximo  # Avança para o próximo nó

# Testes para Lista Encadeada Simples
print("Testando Lista Encadeada Simples")
lista_simples = ListaEncadeada()
lista_simples.insereInicio(1)
lista_simples.insereInicio(2)
lista_simples.insereInicio(3)
lista_simples.mostrar()  # Exibe todos os elementos da lista
print()
lista_simples.excluir_inicio()  # Exclui o primeiro nó
lista_simples.mostrar()  # Exibe a lista após a exclusão
print()
lista_simples.pesquisa(4)  # Tenta pesquisar um valor não presente
print("Excluindo posição 2")
lista_simples.pesquisa(2)  # Pesquisa o valor 2
lista_simples.excluir_posicao(2)  # Exclui o nó com valor 2
lista_simples.mostrar()  # Exibe a lista após a exclusão

# Testes para Lista Encadeada de Extremidade Dupla
print("\nTestando Lista Encadeada de Extremidade Dupla")
lista_dupla = ListaEncadeadaExtremidadeDupla()
lista_dupla.insere_inicio(10)
lista_dupla.insere_final(20)
lista_dupla.insere_inicio(5)
lista_dupla.mostrar()  # Exibe todos os elementos da lista
print()
# Testando exclusões na lista de extremidade dupla
lista_dupla.excluir_inicio()  # Exclui o primeiro nó
lista_dupla.mostrar()  # Exibe a lista após a exclusão
print()
lista_dupla.excluir_final()  # Exclui o último nó
lista_dupla.mostrar()  # Exibe a lista após a exclusão
