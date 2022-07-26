# Altura e sexo (IF)

PesoIdeal1 = float
PesoIdeal2 = float
Altura = float(input('Digite a sua altura '))
Sexo = int(input('Qual o seu sexo? Digite 1 para FEMININO e 2 para MASCULINO: '))
if Sexo == 1:
    PesoIdeal1 = float(62.1 * Altura) - 44.7
    print ('O seu peso ideal é: ', PesoIdeal1)
elif Sexo == 2:
    PesoIdeal2 = float(72.7 * Altura) - 58
    print('O seu peso ideal é: ', PesoIdeal2)
elif Sexo != 1 or Sexo != 2:
    print('Categoria não encontrada.')
