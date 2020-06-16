a = lambda x, y: x * y

print(a(2,2))

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

print(sorted(lista, key = lambda i: i[0]))

teste = lambda nome : nome + ' é monstrão'

print(teste('Franccesco'))

def mostrar(*args, **kwargs):
    return f'teste'

print(mostrar())