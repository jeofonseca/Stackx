Tempo = 0
PercentualAumento = 0.015
NovoPercentual = PercentualAumento * 2
SalarioInicial = 1000.
NovoSalario = SalarioInicial + SalarioInicial * PercentualAumento
ListaAno = (2001, 2018)
print('\nO funcionário inicial com um salário de R$ 1000. \nNo ano de 2000 o seu salário passou a ser de R$ ', NovoSalario)
for Ano in range(2001, 2018):
    import math
    Tempo += 1
    SalarioIncrementado = NovoSalario * (1 + NovoPercentual) ** Tempo
    print(f'A partir do ano de {Ano} o seu salário passou a ser de R$ ', SalarioIncrementado)