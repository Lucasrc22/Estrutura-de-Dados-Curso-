numProvas = 1
Media = 0
for numProvas in range(1,6):
    Nota = float(input("Digite suas notas: "))
    Media += Nota
NotaFinal = Media/5

print(f"Sua Média das 5 foi: {NotaFinal}")
print('Testando agora com método "While""')


MediaWhile = 0
n = 1
while n < 6:
    Nota2= float(input("Digite suas notas: "))
    MediaWhile += Nota2
    n+=1
NotaFinal2 = MediaWhile/5

print(f"Utilizando While Sua Média das 5 provas foi: {NotaFinal2}")

