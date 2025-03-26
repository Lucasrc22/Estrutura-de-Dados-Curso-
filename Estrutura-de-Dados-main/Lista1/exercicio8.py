
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


n = 35
print(f"Fibonacci de {n} sem memoização: {fibonacci(n)}")


from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci_memo(n):
    if n <= 1:
        return n
    return fibonacci_memo(n - 1) + fibonacci_memo(n - 2)

n = 35
print(f"Fibonacci de {n} com memoização: {fibonacci_memo(n)}")


@lru_cache(maxsize=None)
def fatorial_memo(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial_memo(n - 1)


n = 10
print(f"Fatorial de {n} com memoização: {fatorial_memo(n)}")

import time


start_time = time.time()
print(f"Fibonacci de 35 sem memoização: {fibonacci(35)}")
print("Tempo de execução sem memoização: --- %s segundos ---" % (time.time() - start_time))


start_time = time.time()
print(f"Fibonacci de 35 com memoização: {fibonacci_memo(35)}")
print("Tempo de execução com memoização: --- %s segundos ---" % (time.time() - start_time))
