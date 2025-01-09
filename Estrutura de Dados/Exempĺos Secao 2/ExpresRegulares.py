import re

fraseNum = 'Olá, meu numero de telefone é (81)99885-3836'

resultadoNum = re.search(r'\(\d{2}\)\d{4,5}-\d{4}', fraseNum)

if resultadoNum:
    print("Número encontrado:", resultadoNum.group())
else:
    print("Número não encontrado")

print()

frasePlaca = 'A placa de carro que anotei durante o acidente FRT-1998'
re.search('[A-Za-z]{3}-\D{4}',frasePlaca)

resultadoPlaca = re.search('[A-Za-z]{3}-\d{4}',frasePlaca)

if resultadoPlaca:
    print("Placa encontrada: ", resultadoPlaca.group())
else:
    print("Placa não encontrada.")

print()

email= 'Entre em contato, meu email é lucasrios22@hotmail.com'

re.search('\w+@\w+\.com', email)

resultadoEmail = re.search('\w+@\w+\.com', email)
if resultadoEmail:
    print("Email encontrado: ", resultadoEmail.group())
else:
    print('Email não encontrado.')

print()

frase2Placa = 'FRT-1998 é a placa do carro'

print(re.match('[A-Za-z]{3}-\d{4}',frase2Placa))

print()
frase3 = 'Meu número de telefone atual é (81)99885-3836. O número (81)99841-8606 é o antigo'
print(re.findall('\(\d{2}\)\d{4,5}-\d{4}', frase3))

emails = '''Nome: Test1
email: lucas@teste.com
Nome: TEste 2
email: duda@teste.com
NOme2: Maria
email:maria@teste.com.br
'''
print()
print(re.findall('\w+@\w+\.\w*',emails))

