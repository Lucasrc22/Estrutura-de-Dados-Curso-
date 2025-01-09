lista = [1,2,3,4,5]

def linear(n):
    for i in n:
        print(i)
linear(lista)

print()

def quadratic(n):
    for i in n:
        for j in n:
            print(i,j)
        print("----")

quadratic(lista)

def combination(n):
    print(n[0])
    for i in range(5):

        print("test", i)
    for i in n:
        print(i)
    for i in n:
        print(i)
    print("Python")
    print("Python")
    print("Python")
combination(lista)