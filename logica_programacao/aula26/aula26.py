# Operação ternária em Python

while True:
    idade = input('Qual a sua idade?')
    if not idade.isnumeric():
        print('Voce precisa digitar apenas numeros')
    else:
        idade = int(idade)
        e_de_maior = (idade >= 18)
        msg = 'Pode acessar.' if e_de_maior else 'Não pode acessar.'

        print(msg)
        break


"""if idade >= 18:
    print('Pode acessar.')
else:
    print('Não pode acessar.')"""

"""logged_user = True

msg = 'Usuário logado.' if logged_user else 'Usuário precisa logar.'

print(msg)
"""
"""if logged_user:
    msg = 'Usuário logado.'
else:
    msg = 'Usuário precisa logar.'"""

