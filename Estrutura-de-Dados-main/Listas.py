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
    
    def remover_por_matricula(self, matricula):
        if self.primeiro is None:
            print("Lista vazia")
            return
        
        if self.primeiro.matricula == matricula:
            self.primeiro = self.primeiro.proximo
            if self.primeiro is None:  
                self.ultimo = None
            return
        
        atual = self.primeiro
        while atual.proximo is not None and atual.proximo.matricula != matricula:
            atual = atual.proximo

        if atual.proximo is None:
            print("Matrícula não encontrada")
        else:
            if atual.proximo == self.ultimo: 
                self.ultimo = atual
            atual.proximo = atual.proximo.proximo

    def procurar_nota(self, nota):
        if self.primeiro is None:
            print("Lista Vazia")
            return

        atual = self.primeiro
        nota_encontrada = False

        while atual is not None:
            if atual.nota == nota:
                if atual.nota == 10:
                    print(f"Parabéns!! Achamos uma nota {nota} de {atual.nome}")
                elif 7 <= atual.nota < 10:
                    print(f"Você passou, {atual.nome}!!")
                nota_encontrada = True

            atual = atual.proximo

        if not nota_encontrada:
            print(f"Não encontramos nenhum aluno com a nota {nota}")


# Teste do código

Aluno = ListaEncadeada()
Aluno.inserir("01417176458", 10, "Lucas")
Aluno.inserir("02252360445", 9, "Zuila")
Aluno.inserir("70719240158", 10, "Duda")
Aluno.inserir("18219427478", 7, "Jose")

print("Lista antes da ordenação:")
Aluno.printAluno()

Aluno.ordenar_por_nota()

print("\nLista após ordenação por nota:")
Aluno.printAluno()

Aluno.excluir_inicio()
print("\nLista com o primeiro aluno da nota 10 excluído\n")
Aluno.printAluno()

Aluno.remover_por_matricula("02252360445")

print("\nLista após remover matrícula 02252360445:\n")
Aluno.printAluno()

Aluno.procurar_nota(7)
print()
Aluno.procurar_nota(10)
