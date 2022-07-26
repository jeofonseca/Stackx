# Triângulo (IF)

MedidaLado1 = (input('Digite a medida do primeiro lado do triângulo '))
MedidaLado2 = (input('Digite a medida do segundo lado do triângulo '))
MedidaLado3 = (input('Digite a medida do terceiro lado do triângulo '))

if MedidaLado1 == MedidaLado2 and MedidaLado2 == MedidaLado3:
    print ('O triângulo com todos os lados iguais é chamado de Equilátero')
elif MedidaLado1 == MedidaLado2 or MedidaLado2 == MedidaLado3 or MedidaLado1 == MedidaLado3:
    print ('O triângulo com 2 lados iguais é chamado de Isósceles')
elif MedidaLado1 != MedidaLado2 and MedidaLado2 != MedidaLado3 and MedidaLado1 != MedidaLado3:
    print ('O triângulo com todos os lados diferentes é chamado de Escaleno')


