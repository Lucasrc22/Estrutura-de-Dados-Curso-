class No:
    def __init__(self, matricula, nota, nome):
        self.matricula = matricula
        self.nota = nota
        self.nome = nome
        self.proximo = None
    

    def mostrar_no(self):
        print(f'Matrícula: {self.matricula}, Nome: {self.nota}, Nota: {self.nome}')


class ListaEncadeada:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def inserir(self, matricula, nota, nome):
        novo = No(matricula, nome, nota)
        if self.primeiro is None:
            self.primeiro = novo
            self.ultimo = novo
        else:

            atual = self.primeiro
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo
    def printAluno(self):
        atual = self.primeiro

        while atual is not None:
            atual.mostrar_no() 
            atual = atual.proximo
    
    def excluir_inicio(self):
        if self.primeiro is None:
            print("Lista está vazia")
            return None
        temporario = self.primeiro
        self.primeiro = self.primeiro.proximo
        return temporario
    

Aluno = ListaEncadeada()
Aluno.inserir(1234,10, "fulano")
Aluno.inserir(5678,8, "ciclano")
Aluno.inserir(9876,7, "random")
Aluno.excluir_inicio()
Aluno.printAluno()



