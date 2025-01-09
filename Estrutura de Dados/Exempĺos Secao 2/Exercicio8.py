#Crie um dicionário para armazenar o nome e a nota de
#3 alunos, fazendo a leitura dos valores por meio de uma estrutura
#de repetição. Depois, crie uma nova estrutura de repetição para
#somar todas as notas e retornar a média


alunos = {}


for i in range(1, 4):
    nome = str(input(f"Digite o nome do aluno {i}: "))
    nota = float(input(f"Digite a nota do aluno {i}: "))
    alunos[nome] = nota

print("Dicionário de alunos e notas:", alunos)
soma = 0

for j in alunos.values():
    soma += j

print("A soma das 3 notas dos alunos foi ",soma)
media = soma/3
print('Média dos alunos foi de ',media)
