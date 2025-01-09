
# EXERCÍCIO 3:
# Leia a idade do usuário e classifique-o em:
# - Criança: 0 a 12 anos
# - Adolescente: 13 a 17 anos
# - Adulto: acima de 18 anos
# - Se o usuário digitar um número negativo, mostrar a mensagem que a idade é inválida.
while True:
    idade = int(input("Digite sua idade:"))

    if idade >=3 and idade <= 12:
        print("Voce é uma criança")
    elif idade >=13 and idade <=17:
        print("Você é um adolescente")
    elif idade >= 18:
        print("Você é um Adulto")
    else:
        print("Idade inválida")
    print()

    

