# Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
s = float(input('Digite o salário do funcionário em reais: '))

if s >= 1250:
    print('O funcionário terá um aumento de 10%' 'e o valor de seu novo salário será {:.2f}'.format(s*1.1))
else:
    print('O funcionário terá um aumento de 15%' 'e o valor de seu novo salário será {:.2f}'.format(s*1.15))