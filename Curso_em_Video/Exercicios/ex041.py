# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoriam, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 20 anos: SÊNIOR
# Acima: MASTER
ano = int(input('Digite o ano de nascimento do atleta: '))
idade = 2024-ano

if idade <= 9:
    print('O atleta tem {} anos e está na categoria MIRIM'.format(idade))
elif idade <= 14:
    print('O atleta tem {} anos e está na categoria INFANTIL'.format(idade))
elif idade <= 19:
    print('O atleta tem {} anos e está na categoria JÚNIOR'.format(idade))
elif idade <= 20:
    print('O atleta tem {} anos e está na categoria SÊNIOR'.format(idade))
else:
    print('O atleta tem {} anos e está na categoria MASTER'.format(idade))