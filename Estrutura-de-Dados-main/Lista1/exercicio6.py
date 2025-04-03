def torres_de_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f"Mova o disco {n} de {origem} para {destino}")
        return
    
    torres_de_hanoi(n - 1, origem, auxiliar, destino)
    
    print(f"Mova o disco {n} de {origem} para {destino}")
    
    torres_de_hanoi(n - 1, auxiliar, destino, origem)

n = 3
torres_de_hanoi(n, "A", "C", "B")

