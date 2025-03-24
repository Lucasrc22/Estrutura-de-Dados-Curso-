import sys
from functools import lru_cache

# Aumentando o limite de recursão (não recomendado em ambientes de produção)
# sys.setrecursionlimit(10000)

# Função recursiva simples de fatorial
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

# Função iterativa para calcular o fatorial
def fatorial_iterativo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Exemplo de recursão de cauda (tail recursion)
def fatorial_tail(n, resultado=1):
    if n == 0:
        return resultado
    else:
        return fatorial_tail(n - 1, resultado * n)

# Função recursiva com memoization (uso de LRU cache)
@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Função para simular recursão usando uma pilha explícita
def fatorial_iterativo_pilha(n):
    pilha = [n]
    resultado = 1
    while pilha:
        atual = pilha.pop()
        if atual > 1:
            resultado *= atual
            pilha.append(atual - 1)
    return resultado

# Função de exemplo que pode causar estouro de pilha (stack overflow)
def chamada_recursiva_infinita():
    return chamada_recursiva_infinita()

# Teste de função recursiva simples
def testar_fatorial():
    print("Fatorial Recursivo de 5:", fatorial(5))

# Teste de função iterativa para fatorial
def testar_fatorial_iterativo():
    print("Fatorial Iterativo de 5:", fatorial_iterativo(5))

# Teste de função com recursão de cauda
def testar_fatorial_tail():
    print("Fatorial Recursivo de Cauda de 5:", fatorial_tail(5))

# Teste de função com memoization
def testar_fibonacci():
    print("Fibonacci de 100:", fibonacci(100))

# Teste de função simulando recursão com pilha explícita
def testar_fatorial_iterativo_pilha():
    print("Fatorial com pilha de 5:", fatorial_iterativo_pilha(5))

# Teste de estouro de pilha
def testar_stack_overflow():
    try:
        chamada_recursiva_infinita()
    except RecursionError as e:
        print("Erro de estouro de pilha (Stack Overflow):", e)

# Chamadas para testar todas as funções
def main():
    print("Testando Fatorial Recursivo:")
    testar_fatorial()

    print("\nTestando Fatorial Iterativo:")
    testar_fatorial_iterativo()

    print("\nTestando Fatorial com Recursão de Cauda:")
    testar_fatorial_tail()

    print("\nTestando Fibonacci com Memoization:")
    testar_fibonacci()

    print("\nTestando Fatorial com Pilha Explícita:")
    testar_fatorial_iterativo_pilha()

    print("\nTestando Estouro de Pilha (Stack Overflow):")
    testar_stack_overflow()

if __name__ == "__main__":
    main()
"""
O Papel da Pilha de Chamadas (Call Stack) em Funções Recursivas
A pilha de chamadas (call stack) é uma estrutura de dados fundamental que armazena informações sobre 
as funções que estão sendo executadas em um programa, incluindo as variáveis locais e o ponto em que a 
execução de cada função deve continuar após o retorno. Em funções recursivas, a pilha de chamadas desempenha 
um papel crucial, pois cada chamada recursiva cria um novo "quadro" (ou "frame") na pilha. 
Esse quadro contém o estado da função naquele ponto da execução, como parâmetros e variáveis locais.

Como a Pilha de Chamadas Funciona com Recursão
Quando uma função recursiva é chamada, a pilha de chamadas armazena o
 estado da execução de cada instância da função. A recursão ocorre quando a 
 função chama a si mesma com diferentes parâmetros até atingir uma condição base (base case). 
 Quando a condição base é atingida, as chamadas recursivas começam a ser "desempilhadas", 
 retornando aos seus estados anteriores, até que a função original seja completamente executada.


 
 Efeito no Desempenho e Consumo de Memória
Desempenho:
O uso de recursão aumenta o número de chamadas de funções e, consequentemente, o número de "quadro de pilha" 
que precisam ser alocados. Cada quadro contém informações como variáveis locais e o endereço de retorno da função, 
o que pode consumir recursos computacionais. Assim, a recursão pode tornar um problema mais lento em termos de desempenho 
em comparação a uma solução iterativa, especialmente quando a profundidade da recursão é grande.

Consumo de Memória:
A pilha de chamadas cresce à medida que a profundidade da recursão aumenta. Cada novo quadro de pilha ocupa uma quantidade de memória. 
Quando a recursão se torna muito profunda, o consumo de memória pode levar a um estouro de pilha (stack overflow), 
que ocorre quando a pilha não tem mais espaço suficiente para armazenar as informações das novas chamadas.
"""