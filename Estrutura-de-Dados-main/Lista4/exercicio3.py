import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        self.raiz = self._inserir_rec(self.raiz, valor)

    def _inserir_rec(self, no, valor):
        if no is None:
            return Node(valor)
        if valor < no.valor:
            no.esquerda = self._inserir_rec(no.esquerda, valor)
        elif valor > no.valor:
            no.direita = self._inserir_rec(no.direita, valor)
        return no

    def excluir(self, valor):
        self.raiz = self._excluir_rec(self.raiz, valor)

    def _excluir_rec(self, no, valor):
        if no is None:
            return no
        if valor < no.valor:
            no.esquerda = self._excluir_rec(no.esquerda, valor)
        elif valor > no.valor:
            no.direita = self._excluir_rec(no.direita, valor)
        else:
            if no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda
            min_no = self._min_valor_no(no.direita)
            no.valor = min_no.valor
            no.direita = self._excluir_rec(no.direita, min_no.valor)
        return no

    def _min_valor_no(self, no):
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

    def em_ordem(self):
        return self._em_ordem_rec(self.raiz)

    def _em_ordem_rec(self, no):
        if no is None:
            return []
        return self._em_ordem_rec(no.esquerda) + [no.valor] + self._em_ordem_rec(no.direita)

    def para_grafo(self):
        G = nx.DiGraph()
        def add_edges(no):
            if no:
                G.add_node(no.valor)
                if no.esquerda:
                    G.add_edge(no.valor, no.esquerda.valor)
                    add_edges(no.esquerda)
                if no.direita:
                    G.add_edge(no.valor, no.direita.valor)
                    add_edges(no.direita)
        add_edges(self.raiz)
        return G

class InterfaceArvore:
    def __init__(self, master):
        self.arvore = ArvoreBinariaBusca()
        self.master = master
        master.title("Árvore Binária de Busca")

        self.label = tk.Label(master, text="Valor:")
        self.label.grid(row=0, column=0)

        self.entry = tk.Entry(master)
        self.entry.grid(row=0, column=1)

        self.btn_inserir = tk.Button(master, text="Inserir", command=self.inserir_valor)
        self.btn_inserir.grid(row=0, column=2)

        self.btn_excluir = tk.Button(master, text="Excluir", command=self.excluir_valor)
        self.btn_excluir.grid(row=1, column=2)

        self.btn_mostrar = tk.Button(master, text="Mostrar em Ordem", command=self.mostrar_em_ordem)
        self.btn_mostrar.grid(row=2, column=1)

        self.texto = tk.Text(master, height=10, width=40)
        self.texto.grid(row=3, column=0, columnspan=3, pady=10)

        self.fig, self.ax = plt.subplots(figsize=(6,4))
        self.canvas = FigureCanvasTkAgg(self.fig, master)
        self.canvas.get_tk_widget().grid(row=0, column=3, rowspan=4, padx=10)

    def inserir_valor(self):
        try:
            valor = int(self.entry.get())
            self.arvore.inserir(valor)
            self.texto.insert(tk.END, f"Inserido: {valor}\n")
            self.entry.delete(0, tk.END)
            self.desenhar_arvore()
        except ValueError:
            messagebox.showerror("Erro", "Digite um número inteiro válido.")

    def excluir_valor(self):
        try:
            valor = int(self.entry.get())
            self.arvore.excluir(valor)
            self.texto.insert(tk.END, f"Excluído: {valor}\n")
            self.entry.delete(0, tk.END)
            self.desenhar_arvore()
        except ValueError:
            messagebox.showerror("Erro", "Digite um número inteiro válido.")

    def mostrar_em_ordem(self):
        lista = self.arvore.em_ordem()
        self.texto.insert(tk.END, "Árvore em ordem: " + ", ".join(map(str, lista)) + "\n")

    def desenhar_arvore(self):
        self.ax.clear()
        G = self.arvore.para_grafo()
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, ax=self.ax, node_color='lightblue', node_size=1000, arrowsize=20)
        self.canvas.draw()

root = tk.Tk()
interface = InterfaceArvore(root)
root.mainloop()
