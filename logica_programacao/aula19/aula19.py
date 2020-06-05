#Iterando strings com while em Python

while True:
    minha_string = input('Digite uma frase: ')
    tamanho_string = len(minha_string)

    c = 0

    contagem_atual = 0
    letra = ''
    while c < tamanho_string:

        qtd_vezes_letra = minha_string.count(minha_string[c])

        if contagem_atual < qtd_vezes_letra and minha_string[c].strip():
            letra = minha_string[c]
            contagem_atual = qtd_vezes_letra

        c += 1

    print(letra, contagem_atual)

"""
    nova_string = ''
    
    if minha_string[c] == 'r':
        nova_string = nova_string + minha_string[c].upper()
    else:
        nova_string += minha_string[c]


print(nova_string)
    """


