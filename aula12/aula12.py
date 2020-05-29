# len - Quantidade de caracteres

user = input('Enter your username: ')
qtd_caracters = len(user)

print(user, qtd_caracters, type(qtd_caracters))

if qtd_caracters < 6:
    print('You need to type at least 6 caracters.')
else :
    print('You were registered in the system.')


print(user.__len__())
print(f'Dobrando esses caracteres deu o resultado de {len(user) + len(user)}')