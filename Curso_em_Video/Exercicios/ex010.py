# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# Considere US$1,00 = R$3,27
n = float(input('Digite quanto dinheiro tem na carteira: '))
print('Com {} reais é possível comprar {} dólares considerando a cotação de US$1,00 = R$3,27'.format(n, n/3.27))