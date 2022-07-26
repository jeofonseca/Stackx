# Compra de maçâs (IF)

QuantidadeMacas = int(input('Digite a quantidade de maçãs compradas '))
if QuantidadeMacas < 12:
    ValorMaca = 0.30
    ValorTotal = QuantidadeMacas * ValorMaca
    print ('O valor total da compra é: R$ ', ValorTotal)
else:
    ValorMaca = 0.25
    ValorTotal = QuantidadeMacas * ValorMaca
    print ('O valor total da compra é: R$ ', ValorTotal)