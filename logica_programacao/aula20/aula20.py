#Estrutura de repetição em Python
#Função range (start=0, stop, step(pular)=1)

texto = 'Python'
nova_string = ''

# continue = pula para o proximo laço
# break - termina o laço

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        break
    else:
        nova_string += letra

print(nova_string)

#c = 0
#
#for numero in range(0, 100, 3):
#    print(numero)
#
#for n in range(100):
#    if n % 8 == 0:
#        print(n)

