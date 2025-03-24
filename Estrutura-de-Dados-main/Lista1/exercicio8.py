# -------------------------------------------------------
# **Memoização e Recursão de Cauda para Otimização de Funções Recursivas**
# -------------------------------------------------------
#
# **Explicação**:
#
# **Memoização**:
# A memoização é uma técnica de otimização usada em funções recursivas que evita a recomputação de resultados já calculados.
# Ela armazena os resultados das chamadas recursivas em uma tabela (geralmente um dicionário ou cache), de modo que, quando
# o mesmo cálculo for necessário novamente, o valor é recuperado diretamente da tabela em vez de ser recalculado. Isso reduz
# significativamente a complexidade de tempo, especialmente em problemas que envolvem subproblemas repetidos, como o cálculo de Fibonacci.
#
# **Recursão de Cauda**:
# A recursão de cauda é um tipo de recursão onde a chamada recursiva ocorre como a última operação de uma função.
# Isso permite que o compilador ou interpretador otimize a execução da recursão, eliminando a necessidade de manter múltiplos
# frames de pilha. Assim, a recursão de cauda pode ser mais eficiente, já que não há o risco de estouro de pilha em muitos casos.
# Porém, o Python não otimiza automaticamente recursão de cauda.
#
#
# **Fibonacci sem Memoização (versão ineficiente)**:
# Uma implementação recursiva simples do cálculo de Fibonacci sem memoização tem um desempenho muito ruim devido à repetição
# de cálculos, o que aumenta exponencialmente o tempo de execução.
#
# -------------------------------------------------------

# Fibonacci sem Memoização
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Teste de Fibonacci sem memoização
n = 35
print(f"Fibonacci de {n} sem memoização: {fibonacci(n)}")

# -------------------------------------------------------

# **Fibonacci com Memoização**:
# Agora, vamos usar a técnica de **memoização** para otimizar a função. Ao armazenar os resultados intermediários, evitamos
# recomputar os mesmos valores várias vezes.

from functools import lru_cache

# Fibonacci com Memoização
@lru_cache(maxsize=None)
def fibonacci_memo(n):
    if n <= 1:
        return n
    return fibonacci_memo(n - 1) + fibonacci_memo(n - 2)

# Teste de Fibonacci com memoização
n = 35
print(f"Fibonacci de {n} com memoização: {fibonacci_memo(n)}")

# -------------------------------------------------------

# **Fatorial com Memoização**:
# Vamos usar a técnica de memoização em uma função recursiva para calcular o **fatorial** de um número.

# Fatorial com Memoização
@lru_cache(maxsize=None)
def fatorial_memo(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial_memo(n - 1)

# Teste de Fatorial com memoização
n = 10
print(f"Fatorial de {n} com memoização: {fatorial_memo(n)}")

# -------------------------------------------------------

# **Comparação de Desempenho**:
# Vamos comparar o desempenho entre a versão sem memoização e a versão com memoização para Fibonacci.

import time

# Teste sem memoização
start_time = time.time()
print(f"Fibonacci de 35 sem memoização: {fibonacci(35)}")
print("Tempo de execução sem memoização: --- %s segundos ---" % (time.time() - start_time))

# Teste com memoização
start_time = time.time()
print(f"Fibonacci de 35 com memoização: {fibonacci_memo(35)}")
print("Tempo de execução com memoização: --- %s segundos ---" % (time.time() - start_time))

# -------------------------------------------------------

# **Resumo das Técnicas**:
#
# - **Memoização**: Armazena os resultados intermediários para evitar o recalculo de subproblemas. Ideal para problemas recursivos
#   que apresentam subproblemas repetitivos.
# - **Recursão de Cauda**: A recursão de cauda é otimizada para evitar o crescimento da pilha de chamadas. Ela deve ser preferida
#   quando a recursão não envolve grandes operações de cálculo, ou quando o problema pode ser resolvido com recursão de cauda
#   (por exemplo, fatorial de cauda ou somatório).
# - **Evitar Recursão em Certos Casos**: Se a profundidade da recursão for muito grande ou o problema não se encaixar bem com
#   a recursão, é melhor usar uma abordagem iterativa para evitar problemas de desempenho e estouro de pilha.
#
# Essas técnicas ajudam a otimizar funções recursivas e evitam problemas de desempenho em cenários de alta complexidade.

