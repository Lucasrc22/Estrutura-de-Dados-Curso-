while True:
    n1 = int(input('Escolha o número 1: '))
    n2 = int(input('Escolha o número 2: '))

    escolha = input('Deseja fazer qual tipo de cálculo? (soma, subtracao, multiplicacao, divisao) ou digite "sair" para encerrar: ').lower()

    if escolha == "sair":
        print("Encerrando o programa.")
        break

    if escolha == "divisao":
        if n2 != 0:
            print(f"Sua divisão = {n1 / n2}")
        else:
            print("Não é possível dividir por zero!")
    elif escolha == "multiplicacao":
        print(f"Sua multiplicação = {n1 * n2}")
    elif escolha == "soma":
        print(f"Sua soma = {n1 + n2}")
    elif escolha == "subtracao":
        print(f"Sua subtração = {n1 - n2}")
    else:
        print("Opção de cálculo inválida!")

    print()
