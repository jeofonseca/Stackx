# Estruturas condicionais e de repetição: Tabuada com entrada do usuário (FOR)

Numero = int(input('Digite o número para ver a respectiva tabuada: '))
for Multiplicador in range(1, 11):
    print(f'{Numero} x {Multiplicador} = {Numero * Multiplicador}')
while True:
    Numero = int(input('\nDigite o número para ver a respectiva tabuada: '))
    for Multiplicador in range(1, 11):
        print(f'{Numero} x {Multiplicador} = {Numero * Multiplicador}')
