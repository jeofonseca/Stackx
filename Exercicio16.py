# Três valores e o maior deles (IF)

Numero1 = int(input('Digite o primeiro número: '))
Numero2 = int(input('Digite o segundo número: '))
Numero3 = int(input('Digite o terceiro número: '))
if Numero1 > Numero2 and Numero1 > Numero3:
    print('O maior número digitado é', Numero1)
elif Numero2 > Numero1 and Numero2 > Numero3:
    print('O maior número digitado é', Numero2)
elif Numero3 > Numero1 and Numero3 > Numero2:
    print('O maior número digitado é', Numero3)