"""def mensagem(saudacao, nome):
    return f'{saudacao}, {nome}'

saudacao = 'Olá aluno'
nome = 'Franccesco'

print(mensagem(saudacao, nome))

def numeros(n1, n2, n3):
    return n1 + n2 + n3

print(numeros(1,2,2))

def porcentual(valor, porcentual):
    return (valor + (valor * porcentual / 100))

resultado = porcentual(50, 10)
print(resultado)"""

def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'fizzbuzz'
    if n % 5 == 0:
        return 'buzz'
    if n % 3 == 0:
        return 'fizz'
    else:
        return n

from random import randint

for i in range(100):
    aleatorio = randint(0, 100)
    print(fb(aleatorio))