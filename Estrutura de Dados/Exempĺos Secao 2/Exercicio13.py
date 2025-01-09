# Crie uma lista vazia e faça a leitura de dois valores do tipo float,
# colocando cada um dos valores nas primeiras posições da lista 
# (o valor1 ficará na posição 0 da lista e o valor2 ficará na posição 1 da lista). 

# Faça a divisão dos dois valores e trate as seguintes exceções:

# - ValueError: se o usuário digitar um caractere inválido.
# - ZeroDivisionError: se o usuário digitar zero e ocorrer erro na divisão.
# - IndexError: caso a divisão seja feita levando em consideração posições que não existem na lista.
# - KeyboardInterrupt: caso o usuário interrompa a execução.
while True:
    try:

        lista = []

        valor1 = float(input('Digite o primeiro numero da lista: '))
        lista.append(valor1)
        valor2 = float(input('digite o segundo numero da lista: '))
        lista.append(valor2)

        print(lista)

        
        div = lista[0]/lista[2]
        
    except ValueError:
        print('Valor inválido')
    except ZeroDivisionError:
        print('Divisao por zero, digite outro numero')
    except IndexError:
        print('Digite um valor numerico')
    except KeyboardInterrupt:
        print('Usuario interrompeu a execucao')
    else:
        print(f'A divisao dos dois elementos foi: {div}')
            
        



            
