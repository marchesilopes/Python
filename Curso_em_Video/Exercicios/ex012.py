# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
p = float(input('Digite o preço do produto: '))
print('O preço do produto é de {} reais. Com desconto de 5%, o preço será de {} reais.'.format(p, p-(p*0.05)))