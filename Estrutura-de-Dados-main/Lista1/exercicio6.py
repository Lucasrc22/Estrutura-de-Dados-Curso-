def torres_de_hanoi(n, origem, destino, auxiliar):
    """
    Resolve o problema das Torres de Hanoi de forma recursiva.

    Parâmetros:
    n        -> número de discos a serem movidos
    origem   -> torre de onde os discos começam
    destino  -> torre para onde os discos devem ser movidos
    auxiliar -> torre auxiliar usada durante o processo
    """

    if n == 1:
        print(f"Mova o disco {n} de {origem} para {destino}")
        return
    
    torres_de_hanoi(n - 1, origem, auxiliar, destino)
    
    print(f"Mova o disco {n} de {origem} para {destino}")
    
    torres_de_hanoi(n - 1, auxiliar, destino, origem)

# Testando com 5 discos
n = 3
torres_de_hanoi(n, "A", "C", "B")

"""
Estratégia da Recursão:

O problema das Torres de Hanoi segue a seguinte estratégia:

Se tivermos apenas 1 disco, movemos diretamente da origem para o destino.
Se tivermos mais de 1 disco:
Movemos n-1 discos da origem para a torre auxiliar.
Movemos o maior disco (n) diretamente para o destino.
Movemos os n-1 discos da torre auxiliar para o destino.

Complexidade:
O número total de movimentos necessários segue a fórmula: 2^n - 1.
Isso significa que o tempo de execução é O(2^n), ou seja, cresce exponencialmente.

Conclusão:
A abordagem recursiva é intuitiva e reflete bem o problema.
A solução iterativa exige mais controle sobre os movimentos e é menos prática.
Para valores grandes de n, a complexidade exponencial torna a solução inviável em termos de tempo.

"""
