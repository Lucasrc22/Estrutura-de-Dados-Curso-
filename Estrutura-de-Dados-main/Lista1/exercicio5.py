import time


# Implementação Recursiva Simples (Ineficiente)
def fibonacci_recursivo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

def fibonacci_memoizado(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    memo[n] = fibonacci_memoizado(n - 1, memo) + fibonacci_memoizado(n - 2, memo)
    return memo[n]

# Implementação Iterativa (Mais Eficiente)
# Diferente da recursiva, essa abordagem usa um laço de repetição para calcular Fibonacci sem precisar empilhar chamadas na memória.
def fibonacci_iterativo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    anterior, atual = 0, 1
    for _ in range(2, n + 1):
        novo = anterior + atual
        anterior, atual = atual, novo
    return atual

# Vamos testar as três abordagens para ver suas diferenças de desempenho
n = 35  # Testamos com 35 pois valores muito altos podem travar a recursão sem memoização

inicio = time.time()
print(f"Fibonacci Recursivo Simples ({n}):", fibonacci_recursivo(n))
print("Tempo:", time.time() - inicio, "segundos")

inicio = time.time()
print(f"Fibonacci Recursivo com Memoização ({n}):", fibonacci_memoizado(n))
print("Tempo:", time.time() - inicio, "segundos")

inicio = time.time()
print(f"Fibonacci Iterativo ({n}):", fibonacci_iterativo(n))
print("Tempo:", time.time() - inicio, "segundos")

"""
📌 Comparação de Eficiência:

1️⃣ **Recursivo Simples:** 
   - Complexidade: O(2ⁿ) → Muito ineficiente para valores grandes.
   - Problema: Muitos cálculos repetidos tornam a execução lenta.
   - Exemplo: fibonacci(35) já demora bastante tempo.

2️⃣ **Recursivo com Memoização:**
   - Complexidade: O(n) → Muito mais eficiente.
   - Solução: Armazena valores já calculados para evitar recalcular.
   - Resultado: Reduz drasticamente o tempo de execução.

3️⃣ **Iterativo:**
   - Complexidade: O(n), igual ao memoizado.
   - Diferença: Usa um loop e ocupa menos memória (não usa pilha de chamadas).
   - Melhor escolha para aplicações reais!

🎯 **Melhoria Proposta:**
   - Podemos usar **Matriz de Transformação** para calcular Fibonacci em O(log n), usando exponenciação de matrizes.
   - Outra abordagem é **Número de Ouro (φ)** para obter um valor aproximado de Fibonacci
"""