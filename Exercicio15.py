# Polígono (IF)

NumeroLados = int(input('Digite a quantidade de lados da figura geométrica: '))
MedidaLado = float(input('Digite a medida do lado em centímetros: '))
if NumeroLados == 3:
    import math
    AreaT = (pow(MedidaLado, 2) * math.sqrt (3)) / 4
    print ('A figura geométrica é um triângulo e sua área é de', AreaT, 'centímetros.')
elif NumeroLados == 4:
    AreaQ = MedidaLado * MedidaLado
    print ('A figura geométrica é um quadrado e sua área é de', AreaQ, 'centímetros.')
elif NumeroLados == 5:
    print('A figura geométrica é um pentágono.')
elif NumeroLados < 3:
    print ('Esta figura geométrica não é um polígono.')
elif NumeroLados > 5:
    print ('Polígono não identificado.')