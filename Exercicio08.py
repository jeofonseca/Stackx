# Número maior (IF)

Numero1 = float(input('Digite o primeiro número '))
Numero2 = float(input('Digite o segundo número '))

while Numero1 != Numero2:
    if Numero1 > Numero2:
        print('O número', Numero1, 'é maior do que o número', Numero2)
    else:
        print('O número', Numero2, 'é maior do que o número', Numero1)
        break
if Numero1 == Numero2:
    print('Os números digitados devem ser diferentes um do outro.')

