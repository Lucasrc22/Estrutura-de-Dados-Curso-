class Triangulo:
    def __init__(self, lado1, lado2, lado3, base, altura):
        self.lado1 = lado1
        self.lado2= lado2
        self.lado3 = lado3
        self.base = base
        self.altura = altura
    def area(self):
        return print((self.base * self.altura) / 2)
    def tipo(self):
        if self.lado1 > self.lado2 + self.lado3:
            return print('não é um triângulo')
        elif self.lado1== self.lado2 or self.lado1 ==self.lado3 or self.lado2 == self.lado3:
            return print("é um trinângulo Isósceles")
        elif self.lado1 == self.lado2 and self.lado1 == self.lado3 and self.lado2 == self.lado3:
            return print("é um triangulo equilatero")
        else:
            return print("Não é um triangulo") 
        

t1 = Triangulo(1, 2, 3, 4, 3)
t2 = Triangulo(3,3,3,3,4)
t3 = Triangulo(7,2,3,6,9)
t1.area()
t1.tipo()
t2.area()
t2.tipo()
t3.area()
t3.tipo()

