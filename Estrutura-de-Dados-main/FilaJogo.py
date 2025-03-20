from queue import Queue
import random

def jogoSorte():
    fila = Queue()
    numero = random.randint(1, 100)

    while True:
        palpite = int(input("Digite um número de 1 a 100: "))

        if palpite == numero:
            print("Parabéns! Você acertou!")
            break
        else:
            fila.put(palpite)
            print("Número errado, continue tentando.")

    
        print("Números já escolhidos:", list(fila.queue))

        if fila.qsize() >= 3:
            dica = random.choice(list(fila.queue))
            print("Dica: um dos números escolhidos foi", dica)

    print("Fim do jogo.")

jogoSorte()
