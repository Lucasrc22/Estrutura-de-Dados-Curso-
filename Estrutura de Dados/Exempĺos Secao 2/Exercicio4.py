#Calcular a média de um aluno que cursou a disciplina de Programação I, a partir da leitura das notas M1, M2 e M3; passando por um cálculo da média aritmética. 
# Após a média calculada, devemos anunciar se o aluno foi aprovado, reprovado ou pegou exame
#- Se a média estiver entre 0.0 e 4.0, o aluno está reprovado
#- Se a média estiver entre 4.1 e 6.0, o aluno pegou exame
#- Se a média for maior do que 6.0, o aluno está aprovado
#- Se o aluno pegou exame, deve ser lida a nota do exame. Se a nota do exame for maior do que 6.0, está aprovado, senão; está reprovado

#Bom trabalho

NotProva1 = float(input("Qual foi sua primeira nota?"))
NotProva2 = float(input("Qual foi sua segunda nota?"))
NotProva3 = float(input("Qual foi sua terceira nota?"))

Media = (NotProva1+NotProva2+NotProva3)/3

if Media >= 0 and Media <= 4:
    print(f"Sua média foi {Media}, logo foi reprovado")
elif Media >=4.1 and Media < 6:
    print(f"Sua média foi {Media}, logo realizará o Exame")
    Exame = float(input("Digite nota do seu exame:"))
    if Exame < 6:
        print(f"Sua nota no exame foi {Exame}, logo foi reprovado no exame")
    else:
        print(f"Sua nota no exame foi {Media}, logo foi Aprovado no exame")
elif Media >=6:
    print(f"Sua média foi {Media}, logo foi Aprovado")
else:
    print("nota inválida")
