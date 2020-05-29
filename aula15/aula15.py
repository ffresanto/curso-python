#Formatando valores em Python
# :s = string
# :d = int
# :f = float

num1 = 1
num2 = 3
divisao = num1 / num2

print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')

nome = 'Franccesco Felipe'
print(f'{nome:s}')

print(f'{num1:0>10}')

num2 = 1150
num3 = 15
print(f'{num2:0^10}')
print(f'{num3:0<10.2f}')
print(f'{num3:.2f}')

print(len(nome))

print(f'{nome:#^50}')

nome_formatado = '{:-<50}'.format(nome)
nome_formatado2 = '{n:->50}'.format(n = nome)
print(nome_formatado)
print(nome_formatado2)

nome1 = 'franccesco'
sobrenome1 = 'Felipe'
nome_completo = '{0:-^50}'.format(nome1.title(), sobrenome1)
print(nome_completo)

print(nome1.lower())
print(nome1.upper())
print(nome1.title())