import sys
from functools import lru_cache

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)


def fatorial_iterativo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


def fatorial_tail(n, resultado=1):
    if n == 0:
        return resultado
    else:
        return fatorial_tail(n - 1, resultado * n)


@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def fatorial_iterativo_pilha(n):
    pilha = [n]
    resultado = 1
    while pilha:
        atual = pilha.pop()
        if atual > 1:
            resultado *= atual
            pilha.append(atual - 1)
    return resultado

def chamada_recursiva_infinita():
    return chamada_recursiva_infinita()


def testar_fatorial():
    print("Fatorial Recursivo de 5:", fatorial(5))


def testar_fatorial_iterativo():
    print("Fatorial Iterativo de 5:", fatorial_iterativo(5))

def testar_fatorial_tail():
    print("Fatorial Recursivo de Cauda de 5:", fatorial_tail(5))


def testar_fibonacci():
    print("Fibonacci de 100:", fibonacci(100))

def testar_fatorial_iterativo_pilha():
    print("Fatorial com pilha de 5:", fatorial_iterativo_pilha(5))

def testar_stack_overflow():
    try:
        chamada_recursiva_infinita()
    except RecursionError as e:
        print("Erro de estouro de pilha (Stack Overflow):", e)

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