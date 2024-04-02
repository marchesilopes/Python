# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por Km rodado.
km = float(input('Digite a quilometragem percorrida pelo carro: '))
dias = float(input('Digite a quantidade de dias pelos quais o carro foi alugado: '))
print('O carro foi alugado por {} dias e percorreu {} quilômetros. O preço a pagar pelo uso é de {} reais'.format(dias, km, ((60*dias)+(0.15*km))))