import numpy as np
import matplotlib.pyplot as plt

# Definir valores para X1
x1 = np.linspace(0, 6, 400)

# Equação X1 + X2 = 5 => X2 = 5 - X1
x2_1 = 5 - x1

# Equação 4X1 + 8X2 = 20 => X2 = (20 - 4X1) / 8
x2_2 = (20 - 4 * x1) / 8

# Equação 3X1 + 2X2 = 18 => X2 = (18 - 3X1) / 2
x2_3 = (18 - 3 * x1) / 2

# Criar o gráfico
plt.figure(figsize=(6,6))

# Plotar as linhas
plt.plot(x1, x2_1, label=r'$X_1 + X_2 = 5$', color='blue')  # Reta X1 + X2 = 5
plt.axvline(x=4, color='red', label=r'$X_1 \leq 4$', linestyle='--')  # Reta X1 = 4 (restrição)
plt.fill_betweenx(np.linspace(0, 6, 400), 0, 6, color='lightgray', label=r'$X_1, X_2 \geq 0$')  # Área X1, X2 >= 0
plt.plot(x1, x2_2, label=r'$4X_1 + 8X_2 = 20$', color='green')  # Reta 4X1 + 8X2 = 20
plt.plot(x1, x2_3, label=r'$3X_1 + 2X_2 = 18$', color='purple')  # Reta 3X1 + 2X2 = 18

# Ajustar os limites dos eixos
plt.xlim(-1, 6)
plt.ylim(-1, 6)

# Adicionar rótulos, título e legendas
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.xlabel(r'$X_1$')
plt.ylabel(r'$X_2$')
plt.title(r'Gráfico das desigualdades e equações')

# Adicionar uma legenda
plt.legend()

# Exibir o gráfico
plt.grid(True)
plt.show()
