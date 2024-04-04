# Faça um programa que leia o ano de nascimento de um jovem e informe, de acodo com sua idade:
# Se ele ainda vai se alistar ao serviço militar
# Se é hora de se alistar
# Se já passou do tempo de se alistar
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

ano = int(input('Digite o ano de nascimento: '))

if (2024-ano) < 18:
    print('Você deverá se alistar em {} anos.'.format(18-(2024-ano)))
elif (2024-ano) == 18:
    print('Já é hora de se alistar.')
else:
    print('Você já ultrapassou {} anos do prazo de alistamento.'.format(2024-ano-18))
