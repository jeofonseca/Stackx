#  Idade para voto (IF)

AnoAtual = int(input('Digite o ano atual '))
AnoNascimento = int(input('Digite o ano em que nasceu '))
IdadeVoto = AnoAtual - AnoNascimento

if IdadeVoto >= 16:
    print('Você possui idade para votar.')
else:
    print ('Você não possui idade para votar')