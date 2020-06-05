# While - estrutura de repetição em Python

"""
while True:
    nome = input('Qual o seu nome: ')
    print(f'Olá {nome}!')
"""
x = 0 #coluna


while x < 10:
    y = 0  # linha
    while y < 5:
        print(f'X vale {x} e Y vale {y}')
        y += 1
    x += 1
"""
while x < 10:
    if x == 3:
        x = x + 1
        continue


    print(x)
    x = x + 1
"""

print('Acabou!')