# FOR / ELSE em Python


variaveis = ['Micael', 'Maria', 'Franccesco']

for lista_variaveis in variaveis:
    print(lista_variaveis)
    if lista_variaveis.lower().startswith('f'):
        break
else:
    print('Não existe uma palavra que começa com F')

"""
for valor in variavel:
    if valor.startswith('F'):
        print('Começa com F', valor)
    else:
        print('Não começa com F', valor)
"""