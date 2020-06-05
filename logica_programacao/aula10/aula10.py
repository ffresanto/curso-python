"""
Operadores relacionais + IF/ELIF/ELSE
== > >= < <= !=
"""



nome = input('Digite seu nome: ')
idade = input('Qual sua idade: ')

#Limite de idade para pegar emprestimo
idade_menor = 20 # muito jovem
idade_maior = 30 # passou da idade

idade = int(idade) #casting para converter para int

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o emprestimo')
else:
    print(f'{nome} NÃO pode pegar emprestimo')
