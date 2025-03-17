class No:
    def __init__(self, matricula, nota, nome):
        self.matricula = matricula
        self.nota = nota
        self.nome = nome
        self.proximo = None
    
    def mostrar_no(self):
        print(f'Matrícula: {self.matricula}, Nome: {self.nome}, Nota: {self.nota}')

class ListaEncadeada:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def inserir(self, matricula, nota, nome):
        novo = No(matricula, nota, nome)
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

    def ordenar_por_nota(self):
        if self.primeiro is None or self.primeiro.proximo is None:
            return  
        
        trocado = True
        while trocado:
            trocado = False
            atual = self.primeiro
            while atual.proximo is not None:
                if atual.nota < atual.proximo.nota:
                    atual.matricula, atual.proximo.matricula = atual.proximo.matricula, atual.matricula
                    atual.nota, atual.proximo.nota = atual.proximo.nota, atual.nota
                    atual.nome, atual.proximo.nome = atual.proximo.nome, atual.nome
                    trocado = True
                atual = atual.proximo

Aluno = ListaEncadeada()
Aluno.inserir(1234, 10, "Fulano")
Aluno.inserir(5678, 8, "Ciclano")
Aluno.inserir(9876, 7, "Random")
Aluno.inserir(4321, 9, "Beltrano")

print("Lista antes da ordenação:")
Aluno.printAluno()

Aluno.ordenar_por_nota()

print("\nLista após ordenação por nota:")
Aluno.printAluno()

Aluno.excluir_inicio()
print("\nLista com o primeiro aluno da nota 10 excluido\n")
Aluno.printAluno()