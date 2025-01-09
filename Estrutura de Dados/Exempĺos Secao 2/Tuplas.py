tupla = ('Homo sapienas','Canis familiaris','Felis catus')

print(tupla[0])
print()

print(tupla.index('Canis familiaris'))
print()
for elemento in tupla:
    print(elemento)
print()
l1 = ['Homo sapienas','Canis familiaris','Felis catus']
l2 = ['Xenopus laevis','Ailuropoda melanoleuca']
l13= l1+l2
print(l13)

print()
l2_2 = l2*2
print(l2_2)

print()
l1.append('Gorila gorila')
print(l1)
print()
l1.remove('Felis catus')
print(l1)

print()

for item in l2_2:
    print(item)