a = 'casaco'

print(a)

maiuscula = a.upper()
print(maiuscula)

minuscula = maiuscula.lower()

print(minuscula)

capital = a.capitalize()
print(capital)

metade_palavra = a[0:3]
print(metade_palavra)

ultimas_letras = a[3:]

print(ultimas_letras)

b = a.replace('aco', 'inha')

print(a)
print(b)

print(a.find('s'))
print(b.find('a'))

e = ' casaco '
print(len(e))

f=e.strip()

print(len(f))

n1 = 14
n2 = 16

print(f'Dividindo {n1} por {n2} o resultado é {n1/n2}')