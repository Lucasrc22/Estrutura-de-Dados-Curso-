
def LerValores():
    TEMPO = float(input("Qual foi seu tempo de viagem?"))
    VELOCIDADE = float(input("Qual foi sua velocidade média? "))
    
    return TEMPO, VELOCIDADE

def CalculaDistancia(TEMPO, VELOCIDADE):
    DISTANCIA = TEMPO*VELOCIDADE
    return DISTANCIA

def QuantLitros(DISTANCIA):
    LITROS_USADOS = DISTANCIA/12
    return LITROS_USADOS


def PrintResultado(LITROS_USADOS,DISTANCIA,TEMPO,VELOCIDADE):
    print(f"A velocidade média é de {DISTANCIA/TEMPO} metros/segundo")
    print(f"O tempo Gasto utilizado foi de {TEMPO}")
    print(f"a distância percorrida foi de {DISTANCIA}")
    print(f"a quantidade de litros utilizados foi {LITROS_USADOS} na viagem")

def Iniciar():
    TEMPO, VELOCIDADE = LerValores()
    DISTANCIA = CalculaDistancia(TEMPO,VELOCIDADE)
    LITROS_USADOS = QuantLitros(DISTANCIA)
    PrintResultado(LITROS_USADOS,DISTANCIA,TEMPO, VELOCIDADE)
    
Iniciar()
