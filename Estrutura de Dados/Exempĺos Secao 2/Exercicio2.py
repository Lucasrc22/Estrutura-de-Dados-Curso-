gasto_automovel = 12

tempo = float(input('Qual foi seu tempo médio(em horas): '))
velocidade = float(input('Qual sua velocidade média(em Km/H):'))

distancia = tempo * velocidade

litros_utilizados = distancia/gasto_automovel

print(f'sua velocidade média: {velocidade} km/h')
print(f'seu tempo {tempo} horas')
print(f'Sua distancia percorrida {distancia} metros')
print(f'quantidade de litros utilizada: {litros_utilizados} litros')
