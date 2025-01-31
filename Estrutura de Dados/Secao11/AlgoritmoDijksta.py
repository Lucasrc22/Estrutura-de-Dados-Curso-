import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from Secao11.Dijksta import cidades, vertices, arestas

class Dijkstra:
  def __init__(self, vertices, arestas, inicio):
    self.tamanho = len(vertices)
    self.vertices = vertices
    self.grafo = arestas
    self.inicio = inicio

  def mostra_solucao(self, distancias):
    print('Menores distâncias de {} até todos os outros'.format(self.vertices[self.inicio]))
    for vertice in range(self.tamanho):
      print(self.vertices[vertice], distancias[vertice])  

  def distancia_minima(self, distancia, visitados):
    minimo = sys.maxsize
    for vertice in range(self.tamanho):
      if distancia[vertice] < minimo and visitados[vertice] == False:
        minimo = distancia[vertice]
        indice_minimo = vertice
    return indice_minimo

  def dijkstra(self):
    distancia = [sys.maxsize] * self.tamanho
    distancia[self.inicio] = 0
    visitados = [False] * self.tamanho

    for _ in range(self.tamanho):
      indice_minimo = self.distancia_minima(distancia, visitados)
      visitados[indice_minimo] = True
      for vertice in range(self.tamanho):
        if self.grafo[indice_minimo][vertice] > 0 and visitados[vertice] == False \
            and distancia[vertice] > distancia[indice_minimo] + self.grafo[indice_minimo][vertice]:
          distancia[vertice] = distancia[indice_minimo] + self.grafo[indice_minimo][vertice]

    self.mostra_solucao(distancia)
dijkstra = Dijkstra(cidades, arestas, vertices['arad'])
dijkstra.dijkstra()