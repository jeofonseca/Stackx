# Conjunto de valores (While)

contador = 1
resposta = 'sim'
while (resposta == 'sim' or resposta == 's'):
    Numero = float(input('Digite um número maior que zero '))
    Potencia = float(pow(Numero, 2))
    Cubo = float(pow(Numero, 3))
    if Numero <= 0:
        print('O número digitado é menor ou igual a zero. Operação encerrada.')
        break
    import math
    RaizQuadrada = float(math.sqrt(Numero))
    print('O número digitado foi', Numero)
    print('Seu quadrado é', Potencia)
    print('Seu cubo é', Cubo)
    print('E sua raiz quadrada é', RaizQuadrada)
    resposta = input('Deseja continuar?: ')