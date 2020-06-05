# Split, Join e Enumerate em Python

lista = ['Luiz', 'Joao', 'Maria']

for indice, valor in enumerate(lista):
    print(indice, valor)

"""
lista = [
    [0,'Luiz'],
    [1,'Joao'],
    [2,'Maria'],
]

for indice, valor in lista:
    print(indice, valor)
    """

"""
string = 'O Brasil é Penta'
lista = string.split(' ')

for indice, valor in enumerate(lista):
    print(indice, valor, lista[indice])
"""
"""
string2 = ' '.join(lista)

print(string)
print(lista)
print(string2)
"""

"""
string = 'O Brasil é penta.'
lista = string.split(' ')
string2 = ''

print(lista)
"""


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