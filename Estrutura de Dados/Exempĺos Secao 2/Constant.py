import matplotlib.pyplot as plt
import numpy as np
import math as log

n = np.linspace(1, 10, 1000)

# Rótulos para as curvas
labels = ['Constante', 'Logarítmica', 'Linear', "Log Linear", 'Quadrática', 'Cúbica', 'Exponencial']

# Funções Big-O
big_o = [np.ones(n.shape), np.log(n), n, n * np.log(n), n**2, n**3, 2**n]

# Configurando o gráfico
plt.figure(figsize=(10, 8))
plt.ylim(0, 100)  # Limite no eixo Y para visualização

# Plotando as funções
for i in range(len(big_o)):
    plt.plot(n, big_o[i], label=labels[i])

# Adicionando a legenda e os rótulos dos eixos
plt.legend()
plt.ylabel("Y")
plt.xlabel("X")
plt.title("Gráfico de Comparação de Complexidade Big-O")

# Exibindo o gráfico
plt.show()
