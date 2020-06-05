"""hora = input('Que horas são? ')
hora = int(hora)

if hora >= 0 and hora <= 11:
    print('Bom dia')
elif hora >= 12 and hora <= 17:
    print('Boa tarde')
else:
    print('Boa noite')"""

horario = input('Digite um horário (0-23): ')

if horario.isdigit():
    horario = int(horario)

    if horario < 0 or horario > 23:
        print('Horario deve estar entre 0 e 23')
    else:
        if horario <= 11:
            print('Bom dia!')
        elif horario <= 17:
            print('Boa tarde')
        else:
            print('Boa noite!')
else:
    print('Por favor, digite um horario entre 0 e 23')