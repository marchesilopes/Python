# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor
# da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
valor = float(input('Qual o valor da casa? '))
salario = float(input('Qual o salário? '))
anos = int(input('Qual o prazo do financiamento? '))

if (valor/anos) > (salario*0.3):
    print('Não é possível realizar o empréstimo!')
else:
    print('Empréstimo aprovado! O valor da prestação será de {} reais'.format(valor/anos))