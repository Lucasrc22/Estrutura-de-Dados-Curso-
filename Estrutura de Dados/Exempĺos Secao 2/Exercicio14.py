


alunos = {'Pedro': 8.0, 'Maria': 10.0, 'Amilton': 7.5}

with open('Exercicio14.txt','w')as texto:
    for nome, nota in alunos.items():
        texto.write(f'aluno: {nome} e a nota do aluno: {nota}\n')
        texto.write('')
with open('Exercicio14.txt','r')as texto:
    for linha in texto:
        print(linha)