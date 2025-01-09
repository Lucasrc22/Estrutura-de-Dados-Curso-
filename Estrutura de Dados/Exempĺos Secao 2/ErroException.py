while True:
    try:
        n = int(input('digite um numero inteiro: '))
    except ValueError:
        print('valor invalido')
    except KeyboardInterrupt:
        print('usuario interrompeu a execucao')
    else:
        print(f'valor digitado {n}')