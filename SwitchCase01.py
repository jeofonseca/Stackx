# Estruturas condicionais e de repetição: Preço de produtos (Switch Case)

Preco = float(input('Digite o preço do produto: R$ '))
Imposto1 = 0.05
Imposto2 = 0.08
Categoria = int(input('\nEscolha a categoria do produto. \nDigite 1 para Limpeza, 2 para Vestuário ou 3 pra Alimentação: '))
while(Categoria != 1 and Categoria != 2 and Categoria != 3):
    print('\nCategoria inválida!')
    Categoria = int(input('Escolha a categoria do produto. \nDigite 1 para Limpeza, 2 para Vestuário ou 3 pra Alimentação: '))

match Categoria:
    case 1:
        print("\nVocê selecionou a categoria 'Limpeza'")
        if Preco <= 25:
            PercentualAumento = 0.05
            PrecoAumento = Preco + Preco * PercentualAumento
            print('O preço atualizado é: R$ ', PrecoAumento)
        else:
            PercentualAumento = 0.12
            PrecoAumento = Preco + Preco * PercentualAumento
            print('O preço atualizado é: R$ ', PrecoAumento)
    case 2:
        print("\nVocê selecionou a categoria 'Vestuário'")
        if Preco <= 25:
            PercentualAumento = 0.08
            PrecoAumento = Preco + Preco * PercentualAumento
            print('O preço atualizado é: R$ ', PrecoAumento)
        else:
            PercentualAumento = 0.15
            PrecoAumento = Preco + Preco * PercentualAumento
            print('O preço atualizado é: R$ ', PrecoAumento)
    case 3:
        print("\nVocê selecionou a categoria 'Alimentação'")
        if Preco <= 25:
            PercentualAumento = 0.10
            PrecoAumento = Preco + Preco * PercentualAumento
            print('O preço atualizado é: R$ ', PrecoAumento)
        else:
            PercentualAumento = 0.18
            PrecoAumento = Preco + Preco * PercentualAumento
            print('O preço atualizado é: R$ ', PrecoAumento)

Situacao = str(input("\nEntre com a situação do produto. \nDigite 'R' se o produto necessita refrigeração ou 'N' caso não necessite: "))
while(Situacao != 'R' and Situacao != 'r' and Situacao != 'N' and Situacao != 'n'):
    print('\nOpção inválida. Tente novamente!')
    Situacao = str(input("Entre com a situação do produto. \nDigite 'R' se o produto necessita refrigeração ou 'N' caso não necessite: "))
if Situacao == 'R' or Situacao == 'r':
    print('\nO produto necessita de refrigeração.')
else:
    print('\nO produto não necessita de refrigeração.')

if Categoria == 2 and Situacao == 'R' and Situacao == 'r':
        Imposto = Imposto1
        NovoPreco = Preco + PrecoAumento + Imposto
        if NovoPreco <= 50:
            print('\nO preço final do produto é: R$ ', NovoPreco)
            print('Classificação: Barato.')

        if NovoPreco > 50 and NovoPreco < 120:
            print('\nO preço final do produto é: R$ ', NovoPreco)
            print('Classificação: Preço Normal.')

        if NovoPreco > 120:
            print('\nO preço final do produto é: R$ ', NovoPreco, )
            print('Classificação: Caro.')

else:
     Imposto = Imposto2
     NovoPreco = Preco + PrecoAumento + Imposto
     if NovoPreco <= 50:
         print('\nO preço final do produto é: R$ ', NovoPreco)
         print('Classificação: Barato.')

     if NovoPreco > 50 and NovoPreco < 120:
         print('\nO preço final do produto é: R$ ', NovoPreco)
         print('Classificação: Preço Normal.')

     if NovoPreco > 120:
         print('\nO preço final do produto é: R$ ', NovoPreco)
         print('Classificação: Caro.')