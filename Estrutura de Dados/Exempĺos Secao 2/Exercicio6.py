#Questao6 crie uma tabuada de 1 a 10x do numero escolhido pelo usuario

Num = int(input("Digite um número para criarmos a taboada de 1 a 10(Método For in):"))

for n in range(1,11):
    print(f"{Num} x {n} = ", Num*n)
print()

Num2 = int(input("Digite um número para criarmos a taboada de 1 a 10: (Método While): "))

m = 1
while m <11:
    print(f"{Num2} x {m} = ", Num2*m)
    m +=1
