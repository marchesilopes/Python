# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
# pagamento:
# À vista dinheiro/cheque: 10% de desconto
# À vista cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# Em 3x ou mais no cartão: 20% de juros
p = float(input('Digite o preço do produto: '))
print('ESCOLHA A CONDIÇÃO DE PAGAMENTO')
print('[1] À vista dinheiro/cheque: 10% de desconto')
print('[2] À vista cartão: 5% de desconto')
print('[3] Em até 2x no cartão: preço normal')
print('[4] Em 3x ou mais no cartão: 20% de juros')
c = int(input('Digite a condição de pagamento escolhida: '))

if c == 1:
    print('O pagamento será à vista em dinheiro/cheque. O preço do produto é {} reais, você terá 10''%'' de desconto, assim o preço final será de {} reais.'.format(p, p-p*0.1))
elif c == 2:
    print('O pagamento será à vista no cartão. O preço do produto é {} reais, você terá 5''%'' de desconto, assim o preço final será de {} reais.'.format(p, p-p*0.05))
elif c == 3:
    print('O pagamento será em até 2x no cartão. O preço do produto é {} reais, você não terá desconto, assim o preço final será de {} reais.'.format(p, p))
elif c == 4:
    print('O pagamento será em até 3x ou mais no cartão. O preço do produto é {} reais, você terá 20''%'' de juros, assim o preço final será de {} reais.'.format(p, p*1.2))


