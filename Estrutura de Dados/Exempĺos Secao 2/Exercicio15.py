#Para revisar o conteúdo prático sobre expressões regulares, 
#implemente o exercício abaixo. Logo em seguida você pode acessar a aula em vídeo com a solução

#Crie expressões regulares para extrair as seguintes informações do texto abaixo (use a função findall):
#- Números
#- CEPs
#- URLs

import re

Frase = 'Eu tenho 24 anos ,O CEP da minha residencia é 54450-020, ,O endereço da página do curso é https://www.udemy.com/course/estrutura-de-dados-e-algoritmos-python-guia-completo/learn/lecture/20995884#overview'


print('Número encontrado: ', re.findall(r'\d',Frase))
print('CEP encontrado: ', re.findall(r'\b\d{5}-\d{3}\b', Frase))
print('URL encontrada:', re.findall(r'https?://[^\s]+', Frase))