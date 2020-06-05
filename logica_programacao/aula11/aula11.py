"""
Operadores lógicos + IF/ELIF/ELSE
"""
"""
a = 1
b = 2

if not b > a:
    print('Verdadeiro')
else:
    print('Falso')

nome = 'Franccesco Felipe'

if 'e' in nome:
    print('Existe a letra "E" no nome.')
else:
    print('Não existe a letra "E" no nome.')
"""

usuario_adm = 'admin'
senha_adm = '123456'

print('[ LOGIN SISTEMA PY ]')
usuario = input('Usuario: ')
senha = input('Senha: ')

if usuario_adm == usuario and senha_adm == senha:
    print('Usuário logado com sucesso.')
    print('--------Bem vindo!---------')
else:
    print('Usuário ou senha invalida!')
    print('---------------------------')

