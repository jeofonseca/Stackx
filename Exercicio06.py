#  Receber nomes e salários (While)

Meses = 0
SalarioCarlos = float(input('Digite o salário do funcionário Carlos: '))
SalarioJoao = float(SalarioCarlos * 0.30)
RendaJoão = 0.05 * SalarioJoao
RendaCarlos = 0.02 * SalarioCarlos
InvestimentoCarlos = float(SalarioCarlos + RendaCarlos)
InvestimentoJoao = float(SalarioJoao + RendaJoão)

while True:
    Meses += 1
    print(f'O valor de investimentos do João é: R$ {InvestimentoJoao:,.2f}. Seu investimento irá se igualar ao de Carlos no mês', Meses)
    if InvestimentoJoao < InvestimentoCarlos:
        InvestimentoJoao = InvestimentoJoao + RendaJoão
        continue
    else:
        break


