coleta = {'Mosquito': 32, 
          'Albopictus': 22,
          'Darlingi': 14}
print(coleta['Mosquito'])

coleta['montenegrensis'] = 11

print(coleta)
print()
del(coleta['Mosquito'])
print(coleta)

coleta2 = {'gambiae': 13,
           'Deaneorum': 14}

coleta.update(coleta2)

print(coleta)
print()

coleta.items()

for especies, numEspecies in coleta.items():
    print(f'Especie: {especies}, numero de especimes coletados: {numEspecies}')

print()
print()
biomoleculas = ['proteinas', 'gorduras', 'carboidratos', 'vitaminas', 'minerais', 'carboidratos', 'carboidratos']

print(set(biomoleculas))
print()

c1 = {1,2,3,4,5}
c2 = {5,7,8,9,10}

c3 = c1.intersection(c2)
print(c3)
print(c1.difference(c2))