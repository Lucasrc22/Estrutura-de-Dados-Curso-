# Fatorial usando recursão
def fatorial(m):
    if m == 0 or m == 1:  # Caso base: fatorial de 0 ou 1 é 1
        return 1
    else:
        return m * fatorial(m - 1)  # Chamada recursiva

# Testando a função fatorial
print(fatorial(5))  # Deve imprimir 120 (5 * 4 * 3 * 2 * 1)
print(fatorial(0))  # Deve imprimir 1 (fatorial de 0 é 1)
print(fatorial(1))  # Deve imprimir 1 (fatorial de 1 é 1)
print(fatorial(7))  # Deve imprimir 5040

def exponencial(base, expoente):
    if expoente == 0:  # Caso base: qualquer número elevado a 0 é 1
        return 1
    elif expoente == 1:  # Caso base: qualquer número elevado a 1 é ele mesmo
        return base
    elif expoente > 1:  # Passo recursivo para expoente positivo
        return base * exponencial(base, expoente - 1)
    else:  # Passo recursivo para expoente negativo
        return 1 / exponencial(base, -expoente)

# Testando a função exponencial
print(exponencial(2, 3))   # Deve imprimir 8 (2^3)
print(exponencial(5, 0))   # Deve imprimir 1 (5^0)
print(exponencial(3, -2))  # Deve imprimir 0.111... (1 / 3^2)
print(exponencial(7, 1))   # Deve imprimir 7 (7^1)


