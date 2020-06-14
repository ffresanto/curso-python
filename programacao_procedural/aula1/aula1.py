#Funções (def) em Python

"""def saudacao(msg='Olá', nome='Usuario'):
    nome = nome.replace('c', '5')
    msg = msg.replace('O', '1')
    return f'{msg} {nome}'

variavel = saudacao()

print(variavel)"""

"""def funcao(var):
    print(var)

variavel = funcao('teste')

print(variavel)"""

"""def divisao(n1, n2):
    if n2 == 0:
        return

    return n1 / n2

divide = divisao(8, 0)

if divide:
    print(divide)
else:
    print('Conta invalida')"""

"""def dumb():
    return [1,2,3,4,5]

print(dumb(), type(dumb()))
"""

"""def f(var):
    print(var)

def dumb():
    return f
"""
def func(*args):
    print(args)
    print(args[0])
    print(args[3])

func(1,2,3,4,5)

lista = [1,2,3,4,5]
print(*lista, sep='-')
print(1,2,3,4,5)