def soma1(n):
    soma = 0
    for i in range(n+1):
        soma += i
    return print(soma)

soma1(5)

def soma2(n):
    if n == 0:
        return 0
    return print(n + soma2(n-1))
