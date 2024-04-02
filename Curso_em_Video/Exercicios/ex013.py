# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
s = float(input('Digite o salário em reais: '))
print('O valor do salário é {:.2f}. Com um aumento de 15%, o novo salário será de {:.2f} reais'.format(s, s*1.15))