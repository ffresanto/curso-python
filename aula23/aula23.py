# Split, Join e Enumerate em Python

string = 'O Brasil é penta.'
lista = string.split(' ')
string2 = ''

print(lista)


""" Split
string = 'O Brasil é o pais do futebol, o Brasil Brasil é penta.'
lista_1 = string.split(' ')
lista_2 = string.split(',')

for valor in lista_2:
    print(valor.strip())
"""
"""
palavra = ''
contagem = 0

for lista_tudo in lista_1:
    qtd_vezes = lista_1.count(lista_tudo)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = lista_tudo

print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')
"""