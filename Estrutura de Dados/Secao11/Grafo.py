import sys
import os

# Adiciona o diretório raiz ao caminho de busca
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from Secao6.Pilhas import Pilha
from Secao6.Fila import FilaCircular
from Secao6.VetorOrdenado import VetorOrdenado


class Vertice:
    def __init__(self, rotulo, distancia_objetivo):
        self.rotulo = rotulo
        self.visitado = False
        self.adjacentes= []
        self.distancia_objetivo = distancia_objetivo


    def adiciona_adjacente(self, adjacente):
        self.adjacentes.append(adjacente)
    
    def mostra_adjacente(self):
        for i in self.adjacentes:
            print(i.vertice.rotulo, i.custo)

class Adjacente:
    def __init__(self, vertice, custo):
        self.vertice = vertice
        self.custo = custo
        self.distancia_aestrela = vertice.distancia_objetivo + self.custo
class Gulosa:
  def __init__(self, objetivo):
    self.objetivo = objetivo
    self.encontrado = False

  def buscar(self, atual):
    print('-------')
    print('Atual: {}'.format(atual.rotulo))
    atual.visitado = True

    if atual == self.objetivo:
      self.encontrado = True
    else:
      vetor_ordenado = VetorOrdenado(len(atual.adjacentes))
      for adjacente in atual.adjacentes:
        if adjacente.vertice.visitado == False:
          adjacente.vertice.visitado == True
          vetor_ordenado.insere(adjacente.vertice)
      vetor_ordenado.imprime()

      if vetor_ordenado.valores[0] != None:
        self.buscar(vetor_ordenado.valores[0])

class Grafo:
  arad = Vertice('Arad', 366)
  zerind = Vertice('Zerind', 374)
  oradea = Vertice('Oradea', 380)
  sibiu = Vertice('Sibiu', 253)
  timisoara = Vertice('Timisoara', 329)
  lugoj = Vertice('Lugoj', 244)
  mehadia = Vertice('Mehadia', 241)
  dobreta = Vertice('Dobreta', 242)
  craiova = Vertice('Craiova', 160)
  rimnicu = Vertice('Rimnicu', 193)
  fagaras = Vertice('Fagaras', 178)
  pitesti = Vertice('Pitesti', 98)
  bucharest = Vertice('Bucharest', 0)
  giurgiu = Vertice('Giurgiu', 77)

  arad.adiciona_adjacente(Adjacente(zerind, 75))
  arad.adiciona_adjacente(Adjacente(sibiu, 140))
  arad.adiciona_adjacente(Adjacente(timisoara, 118))

  zerind.adiciona_adjacente(Adjacente(arad, 75))
  zerind.adiciona_adjacente(Adjacente(oradea, 71))

  oradea.adiciona_adjacente(Adjacente(zerind, 71))
  oradea.adiciona_adjacente(Adjacente(sibiu, 151))

  sibiu.adiciona_adjacente(Adjacente(oradea, 151))
  sibiu.adiciona_adjacente(Adjacente(arad, 140))
  sibiu.adiciona_adjacente(Adjacente(fagaras, 99))
  sibiu.adiciona_adjacente(Adjacente(rimnicu, 80))

  timisoara.adiciona_adjacente(Adjacente(arad, 118))
  timisoara.adiciona_adjacente(Adjacente(lugoj, 111))

  lugoj.adiciona_adjacente(Adjacente(timisoara, 111))
  lugoj.adiciona_adjacente(Adjacente(mehadia, 70))

  mehadia.adiciona_adjacente(Adjacente(lugoj, 70))
  mehadia.adiciona_adjacente(Adjacente(dobreta, 75))

  dobreta.adiciona_adjacente(Adjacente(mehadia, 75))
  dobreta.adiciona_adjacente(Adjacente(craiova, 120))

  craiova.adiciona_adjacente(Adjacente(dobreta, 120))
  craiova.adiciona_adjacente(Adjacente(pitesti, 138))
  craiova.adiciona_adjacente(Adjacente(rimnicu, 146))

  rimnicu.adiciona_adjacente(Adjacente(craiova, 146))
  rimnicu.adiciona_adjacente(Adjacente(sibiu, 80))
  rimnicu.adiciona_adjacente(Adjacente(pitesti, 97))

  fagaras.adiciona_adjacente(Adjacente(sibiu, 99))
  fagaras.adiciona_adjacente(Adjacente(bucharest, 211))

  pitesti.adiciona_adjacente(Adjacente(rimnicu, 97))
  pitesti.adiciona_adjacente(Adjacente(craiova, 138))
  pitesti.adiciona_adjacente(Adjacente(bucharest, 101))

  bucharest.adiciona_adjacente(Adjacente(fagaras, 211))
  bucharest.adiciona_adjacente(Adjacente(pitesti, 101))
  bucharest.adiciona_adjacente(Adjacente(giurgiu, 90))



grafo = Grafo()
grafo.arad.mostra_adjacente()
print()
grafo.bucharest.mostra_adjacente()
print()
grafo.pitesti.mostra_adjacente()

class BuscaProfundidade:
    def __init__(self, inicio):
        self.inicio = inicio
        self.inicio.visitado = True
        self.pilha = Pilha(20)
        self.pilha.empilhar(inicio)
    
    def buscar(self):
        topo = self.pilha.verTopo()
        print('Topo: {}'.format(topo.rotulo))
        for adjacente in topo.adjacentes:
            print(('Topo é {}. {} já foi visitada? {}'.format(topo.rotulo, adjacente.vertice.rotulo, adjacente.vertice.visitado)))
            if adjacente.vertice.visitado == False:
                adjacente.vertice.visitado = True
                self.pilha.empilhar(adjacente.vertice)
                print('Empilhou {}'.format(adjacente.vertice.rotulo))
                self.buscar()

        print('Desempilhou: {}'.format(self.pilha.desempilhar().rotulo))
        print()
class BuscaLargura:
  def __init__(self, inicio):
    self.inicio = inicio
    self.inicio.visitado = True
    self.fila = FilaCircular(20)
    self.fila.enfileirar(inicio)

  def buscar(self):
    primeiro = self.fila.primeiro()
    print('-------')
    print('Primeiro da fila: {}'.format(primeiro.rotulo))
    temp = self.fila.desenfileirar()
    print('Desenfileirou: {}'.format(temp.rotulo))
    for adjacente in primeiro.adjacentes:
      print('Primeiro era {}. {} já foi visitado? {}'.format(temp.rotulo, adjacente.vertice.rotulo, adjacente.vertice.visitado))
      if adjacente.vertice.visitado == False:
        adjacente.vertice.visitado = True
        self.fila.enfileirar(adjacente.vertice)
        print('Enfileirou: {}'.format(adjacente.vertice.rotulo))
    if self.fila.numero_elementos > 0:
      self.buscar()

class AEstrela:
  def __init__(self, objetivo):
    self.objetivo = objetivo
    self.encontrado = False

  def buscar(self, atual):
    print('----------')
    print('Atual: {}'.format(atual.rotulo))
    atual.visitado = True

    if atual == self.objetivo:
      self.encontrado = True
    else:
      vetor_ordenado = VetorOrdenado(len(atual.adjacentes))
      for adjacente in atual.adjacentes:
        if adjacente.vertice.visitado == False:
          adjacente.vertice.visitado = True
          vetor_ordenado.insere(adjacente)
      vetor_ordenado.imprime()

      if vetor_ordenado.valores[0] != None:
        self.buscar(vetor_ordenado.valores[0].vertice)

buscar_profundidade = BuscaProfundidade(grafo.arad)

buscar_profundidade.buscar()

fila = FilaCircular(20)

fila.enfileirar(grafo.arad)
fila.enfileirar(grafo.bucharest)
fila.enfileirar(grafo.fagaras)
fila.primeiro().rotulo
fila.desenfileirar().rotulo
fila.primeiro().rotulo


busca_largura = BuscaLargura(grafo.arad)
busca_largura.buscar()

busca_gulosa = Gulosa(grafo.bucharest)
busca_gulosa.buscar(grafo.arad)

print()
print()
vetor = VetorOrdenado(5)
vetor.insere(grafo.arad)
vetor.insere(grafo.craiova)
vetor.insere(grafo.bucharest)
vetor.insere(grafo.dobreta)
vetor.imprime()

vetor.insere(grafo.lugoj)
vetor.imprime()

vetor.valores[0], vetor.valores[0].rotulo

busca_aestrela = AEstrela(grafo.bucharest)
busca_aestrela.buscar(grafo.arad)