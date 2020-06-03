#programa para descobrir letra secreta
# digite /encerrar para sair da applicação

secreto = 'celular'
letra_digitada = []
chances = 3

while True:
    if chances <= 0:
        print('Voce perdeu!!!')
        break

    letra = input('Digite uma letra: ')

    if letra == 'encerrar':
        print('Voce encerrou a aplicação.')
        break

    if len(letra) > 1:
        print('Ahhh isso não vale, digite apenas uma letra.')
        continue

    letra_digitada.append(letra)

    if letra in secreto:
        print(f'\nUHUULLL, a letra "{letra}" existe na palavra secreta.\n')
    else:
        print(f'\nPUTZ ERROU: a letra "{letra}" não existe na palavra secreta\n')
        letra_digitada.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in letra_digitada:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Que legal, VOCE GANHOU!!! A palavra era "{secreto_temporario.upper()}"')
        break
    else:
        print(f'A palavra secreta esta assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1
        print(f'\nVoce ainda tem {chances} chances.')

