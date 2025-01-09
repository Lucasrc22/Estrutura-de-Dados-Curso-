with open('/home/guest/Documentos/Estudo/Exempĺos Secao 2/Texto.txt') as tex:
    r = tex.readlines()
    print(r)
    for linha in tex:
        print(linha)

    
with open('Texto2.txt','w')as texto:
    texto.write('Ola a todos')