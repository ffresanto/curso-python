# Índices e fatiamento de strings em Python
#              indicies:
# positivos    [0123456789]
texto        = 'Python s2'
texto2        = 'abcdefghi'
#negativos     [987654321]


url = 'www.google.com.br/'

print(url[:-1])
print(texto[8])
print(len(texto))

nova_string = texto[2:6]
nova_string2 = texto2[0::3]
print(nova_string)
print(nova_string2)

