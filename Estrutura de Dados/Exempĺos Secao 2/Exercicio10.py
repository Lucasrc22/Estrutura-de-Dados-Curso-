
def LerTemperatura():
    TempC = float(input("Digite a temperatura em Celsius: "))
    return TempC

def Calculo(TempC):
    F = (9*TempC + 160)/5
    return F

def printResultado(F, TempC):
    print(f"A temperatura de Celsius {TempC} em Fahrenheit é de {F}")

def LerPrograma():
    Celsius = LerTemperatura()
    Fahrenheit = Calculo(Celsius)
    printResultado(Fahrenheit, Celsius)

LerPrograma()