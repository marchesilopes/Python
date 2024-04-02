# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = str(input('Digite o nome da pessoa: ')).upper().strip()

print('A pessoa tem Silva no nome? {}'.format(nome.find('SILVA')>-1))