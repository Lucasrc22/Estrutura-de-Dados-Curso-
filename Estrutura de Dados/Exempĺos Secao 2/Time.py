import time as tm

tm.time() #tempo da execucao do codigo

antes = tm.time()

lista= []

for i in range(0,1000):
    lista.append(i)
depois = tm.time()

intervalo = depois - antes

print(f' Tempo: {intervalo} segundos')

print('FInalizando')
tm.sleep(2)

print('.....')

tm.sleep(2)
print(lista)
print('Até a próxima')