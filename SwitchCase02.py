# Estruturas condicionais e de repetição: Compra de produto (Switch Case)

Lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Lista2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
Lista3: list[int] = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
Lista4: list[int] = [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
Preco = 0.0

Codigo = int(input('Digite um código entre os números 1 e 40: '))
while(Codigo <= 0 or Codigo > 40):
    print('\nCódigo Inválido.')
    Codigo = int(input('\nDigite um código entre os números 1 e 40: '))

if Codigo in Lista1:
    Preco = 10.
elif Codigo in Lista2:
    Preco = 15.
elif Codigo in Lista3:
    Preco = 20.
elif Codigo in Lista4:
    Preco = 30.

match Codigo:
        case (int(Lista1)):
            print('O produto custa R$', Preco)
        case (int(Lista2)):
            print('O produto custa R$', Preco)
        case(int(Lista3)):
            print('O produto custa R$', Preco)
        case(int(Lista4)):
            print('O produto custa R$', Preco)
Quantidade = int(input('\nDigite a quantidade de produtos comprados: '))

Desconto1 = 0.05
Desconto2 = 0.10
Desconto3 = 0.15

PrecoNota = Preco * Quantidade

if PrecoNota <=250:
    ValorDesconto = PrecoNota * Desconto1
    PrecoFinal = PrecoNota - ValorDesconto
    print('\nO produto custa R$', Preco)
    print('Foram comprados ', Quantidade, 'produtos.')
    print('O preço da nota é R$', PrecoNota)
    print('O valor do desconto é de R$', ValorDesconto)
    print('O preço final da nota é de R$', PrecoFinal)
elif PrecoNota > 250 and PrecoNota <= 500:
    ValorDesconto = PrecoNota * Desconto2
    PrecoFinal = PrecoNota - ValorDesconto
    print('\nO produto custa R$', Preco)
    print('Foram comprados ', Quantidade, 'produtos.')
    print('O preço da nota é R$', PrecoNota)
    print('O valor do desconto é de R$', ValorDesconto)
    print('O preço final da nota é de R$', PrecoFinal)
elif PrecoNota > 500:
    ValorDesconto = PrecoNota * Desconto3
    PrecoFinal = PrecoNota - ValorDesconto
    print('\nO produto custa R$', Preco)
    print('Foram comprados', Quantidade, 'produtos.')
    print('O preço da nota é R$', PrecoNota)
    print('O valor do desconto é de R$', ValorDesconto)
    print('O preço final da nota é de R$', PrecoFinal)