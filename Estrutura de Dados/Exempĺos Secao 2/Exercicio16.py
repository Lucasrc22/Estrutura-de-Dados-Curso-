# Para revisar o conteúdo prático visto até agora, você agora pode resolver um exercício.
# Logo em seguida, você pode acessar a aula em vídeo com a solução.

# Crie uma classe chamada Aluno com os seguintes atributos:
# - Nome
# - Nota 1
# - Nota 2
# - Crie um construtor para a classe (__init__)

class Aluno:
    def __init__(self, Nome, Nota1, Nota2):
        self.Nome = Nome
        self.Nota1 = Nota1
        self.Nota2 = Nota2

    def media(self):
        self.mediaNota = (self.Nota1 + self.Nota2)/2

        return print("Sua média: ", self.mediaNota)
    
    def Resultado(self):
        if self.mediaNota < 6:
            return print("Voce foi reprovado: ", self.Nome)
        elif self.mediaNota >=6:
            return print("Parabéns, voce foi aprovado", self.Nome)
        else:
            return print("Nota inválida")
        
aluno1 = Aluno("Lucas", 8, 9)
aluno2 = Aluno("Maria", 5,5)

aluno1.media()
aluno1.Resultado()
aluno2.media()
aluno2.Resultado()