numero_inteiro = input('Digite um número inteiro: ')

if numero_inteiro.isdigit():
    numero_inteiro = int(numero_inteiro)

    if numero_inteiro % 2 == 0: #formula para saber se o numero é par
        print(f'{numero_inteiro } é Número par')
    else:
        print(f'{numero_inteiro} é Numero impar')
else:
    print('Isso não é um numero inteiro.')