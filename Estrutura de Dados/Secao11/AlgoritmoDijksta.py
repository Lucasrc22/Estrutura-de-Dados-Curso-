import sys
import os

# Adiciona o caminho do diretório pai para permitir importação de módulos externos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

# Importa os dados da matriz de adjacência e dos vértices
from Secao11.Dijksta import cidades, vertices, arestas  

class Dijkstra:
  def __init__(self, vertices, arestas, inicio):
    """
    Construtor da classe Dijkstra.

    Parâmetros:
    - vertices: Dicionário mapeando nomes de cidades para índices numéricos.
    - arestas: Matriz de adjacência contendo as distâncias entre cidades.
    - inicio: Índice do vértice de origem (cidade inicial).
    """
    self.tamanho = len(vertices)  # Número total de cidades (vértices)
    self.vertices = vertices      # Dicionário de cidades
    self.grafo = arestas          # Matriz de adjacência (distâncias entre cidades)
    self.inicio = inicio          # Cidade inicial para calcular as menores distâncias

  def mostra_solucao(self, distancias):
    """
    Exibe as menores distâncias da cidade inicial até todas as outras cidades.
    
    Parâmetros:
    - distancias: Lista contendo a menor distância da cidade inicial até cada cidade.
    """
    print(f'Menores distâncias de {self.vertices[self.inicio]} até todos os outros:')
    for vertice in range(self.tamanho):
      print(self.vertices[vertice], distancias[vertice])  

  def distancia_minima(self, distancia, visitados):
    """
    Retorna o índice do vértice com a menor distância ainda não visitado.

    Parâmetros:
    - distancia: Lista com as menores distâncias calculadas até o momento.
    - visitados: Lista indicando quais cidades já foram processadas.

    Retorno:
    - Índice da cidade com a menor distância atual.
    """
    minimo = sys.maxsize  # Inicializa com um valor muito grande (infinito)
    indice_minimo = -1    # Armazena o índice da cidade com menor distância

    for vertice in range(self.tamanho):
      # Se a distância for menor que o mínimo atual e a cidade ainda não foi visitada
      if distancia[vertice] < minimo and not visitados[vertice]:
        minimo = distancia[vertice]
        indice_minimo = vertice

    return indice_minimo  # Retorna o índice da cidade com menor distância

  def dijkstra(self):
    """
    Implementação do algoritmo de Dijkstra para encontrar as menores distâncias 
    da cidade de origem até todas as outras cidades do grafo.
    """
    distancia = [sys.maxsize] * self.tamanho  # Inicializa todas as distâncias como infinito
    distancia[self.inicio] = 0                # A distância da cidade de origem para ela mesma é 0
    visitados = [False] * self.tamanho        # Lista para rastrear quais cidades já foram processadas

    for _ in range(self.tamanho):
      # Escolhe a cidade com a menor distância que ainda não foi visitada
      indice_minimo = self.distancia_minima(distancia, visitados)
      visitados[indice_minimo] = True  # Marca essa cidade como visitada

      # Atualiza as distâncias para os vizinhos da cidade escolhida
      for vertice in range(self.tamanho):
        if self.grafo[indice_minimo][vertice] > 0 and not visitados[vertice]:
          nova_distancia = distancia[indice_minimo] + self.grafo[indice_minimo][vertice]
          
          # Se a nova distância for menor que a atual, atualiza a distância mínima
          if distancia[vertice] > nova_distancia:
            distancia[vertice] = nova_distancia

    # Exibe os resultados
    self.mostra_solucao(distancia)


# Criando uma instância do algoritmo de Dijkstra e executando-o a partir de 'arad'
dijkstra = Dijkstra(cidades, arestas, vertices['arad'])
dijkstra.dijkstra()
