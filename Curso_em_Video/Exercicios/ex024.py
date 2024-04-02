# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
cidade = str(input('Digite o nome da cidade: ')).upper().strip()

print('O nome da cidade começa com a palavra santo? {}'.format(cidade.find('SANTO')==0))