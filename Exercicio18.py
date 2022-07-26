# Ângulos do triângulo (IF)

Angulo1 = float(input('Digite o valor do primeiro ângulo: '))
Angulo2 = float(input('Digite o valor do segundo ângulo: '))
Angulo3 = float(input('Digite o valor do terceiro ângulo: '))

if Angulo1 == 90 or Angulo2 == 90 or Angulo3 == 90:
    print('Este é um triângulo retângulo.')
elif Angulo1 > 90 or Angulo2 > 90 or Angulo3 > 90:
    print('Este é um triângulo obtusângulo')
else:
    print('Este é um triângulo acutângulo')