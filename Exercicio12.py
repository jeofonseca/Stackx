#  3 valores em ordem (IF)

N1 = int(input('Digite o primeiro número: '))
N2 = int(input('Digite o segundo número: '))
N3 = int(input('Digite o terceiro número: '))

Ordem1 = N1, N2, N3
Ordem2 = N1, N3, N2
Ordem3 = N2, N1, N3
Ordem4 = N2, N3, N1
Ordem5 = N3, N1, N2
Ordem6 = N3, N2, N1

while N1 != N2 != N3:
    if N1 > N2 > N3:
        print('A sequência ordenada dos números digitados é: ', Ordem1)
    elif N1 > N3 > N2:
        print('A sequência ordenada dos números digitados é: ', Ordem2)
    elif N2 > N1 > N3:
        print('A sequência ordenada dos números digitados é: ', Ordem3)
    elif N2 > N3 > N1:
        print('A sequência ordenada dos números digitados é: ', Ordem4)
    elif N3 > N1 > N2:
        print('A sequência ordenada dos números digitados é: ', Ordem5)
    elif N3 > N2> N1:
        print('A sequência ordenada dos números digitados é: ', Ordem6)
    break
