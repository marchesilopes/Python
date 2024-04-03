# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da pasagem, cobrando R$0,50 por
# Km para viagens até 200 Km e R$0,45 para viagens mais longas.

km = float(input('Digite a distância da viagem em km: '))

if km <= 200:
    print('O preço da passagem é de {} reais.'.format(km*0.5))
else:
    print('O preço da passagem é de {} reais.'.format(200*0.5+(km-200)*0.45))