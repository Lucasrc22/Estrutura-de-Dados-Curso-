import time


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


def fibonacci_iterativo(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


n = 35  

inicio = time.time()
print(f"Fibonacci Recursivo Simples ({n}):", fibonacci_recursivo(n))
print("Tempo:", time.time() - inicio, "segundos")

inicio = time.time()
print(f"Fibonacci Recursivo com Memoização ({n}):", fibonacci_memoizado(n))
print("Tempo:", time.time() - inicio, "segundos")

inicio = time.time()
print(f"Fibonacci Iterativo ({n}):", fibonacci_iterativo(n))
print("Tempo:", time.time() - inicio, "segundos")

