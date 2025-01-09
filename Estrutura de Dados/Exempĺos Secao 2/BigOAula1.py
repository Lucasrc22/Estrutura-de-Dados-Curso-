import timeit

def soma1(n):
    soma = 0
    for i in range(n + 1):
        soma += i
    return soma
# Explicação sobre os parâmetros usados no timeit:
# O primeiro parâmetro é uma string contendo a chamada à função soma1(10000).
# globals=globals() garante que o interpretador Python tenha acesso à função soma1 e outras variáveis do escopo global.
# O parâmetro number=100 indica que a função será executada 100 vezes, e o tempo retornado será o total dessas execuções.
# Função timeit para medir o tempo de execução
tempo_execucao = timeit.timeit("soma1(10)", globals=globals(), number=1)
print(f"Tempo de execução: {tempo_execucao:.6f} segundos")

def soma2(n):
    return (n*(n+1)) / 2

tempo_execucao2 = timeit.timeit("soma2(10)", globals=globals(), number=1)
print(f"Tempo de execução da outra função: {tempo_execucao2:.6f} segundos")

