#Desempacotamento de listas em Python

lista = ['Luiz', 'Joao', 'Maria', 1, 2 ,3, 4, 5, 6]

n1, n2, n3, *_ = lista


print(n1, n2)