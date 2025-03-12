import pulp

from scipy.optimize import linprog
# Criar o problema
prob = pulp.LpProblem("Maximizar_Lucro", pulp.LpMaximize)

# Definir as variáveis
x1 = pulp.LpVariable("x1", lowBound=0)
x2 = pulp.LpVariable("x2", lowBound=0)

# Função objetivo
prob += 40 * x1 + 30 * x2

# Restrições
prob += 2 * x1 + x2 <= 100
prob += 3 * x1 + 2 * x2 <= 120

# Resolver o problema
prob.solve(pulp.PULP_CBC_CMD(msg=True))

# Resultados
print(f"Solução ótima: x1 = {x1.varValue}, x2 = {x2.varValue}")
print(f"Lucro ótimo: {pulp.value(prob.objective)}")

# Definir os coeficientes da função objetivo (maximizar -40x1 - 30x2)
c = [-40, -30]

# Definir as desigualdades (matriz A e vetor b)
A = [[2, 1], [3, 2]]
b = [100, 120]

# Definir os limites das variáveis (não-negatividade)
x0_bounds = (0, None)
x1_bounds = (0, None)

# Resolver o problema usando Simplex
result = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='simplex')

# Exibir os resultados
print("Resultado:", result)
