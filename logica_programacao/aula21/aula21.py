#Listas em Python
#append, insert, pop, del, clear, extend, +
#min, max
#range

"""
texto = 'Valor'
lista_teste = [1, 2, 3, 4, 'Franccesco', True, 10.5]

#         0    1    2    3    4
lista = ['A', 'B', 'C', 'D', 'E', 10.5]
#        -5   -4   -3   -2   -1
#lista[5] = 'Qualquer outra coisa.'

print(lista[])
"""
l1 = [1, 2, 3]
l2 = [4, 5, 6]

l1.append('b')
l2.insert(0, 'banana')
l1.extend(l2)

print(l1)
print(l2)
outros = '{:-^50}'.format('outros')
l2.pop() #retira o ultimo valor da lista
print(l2)
print(outros)

#     0 1 2 3 4 5 6 7 8
l3 = [1,2,3,4,5,6,7,8,9]
l4 = list(range(0, 10)) #mesma coisa que o 'l3'

for valor in l4:
    print(valor)

print(l4)
print(max(l3))
print(min(l3))

l3.insert(0, 'Banana')
del(l3[0])

print(outros)

l5 = [0,1,2,3,4,5,6,7,8,9]
l6 = ['String', True, 10, -20.5]

for elem in l6:
    print(f'O tipo de {elem} é {type(elem)} e seu valor é {elem}')


soma = 0
for valor in l5:
    soma = soma + valor

print(soma)

print(outros)


