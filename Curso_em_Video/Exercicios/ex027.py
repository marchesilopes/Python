# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

nome = str(input('Digite o nome de uma pessoa: ')).split()

n = len(nome)

print('O primeiro nome desta pessoa é {}.'.format(nome[0]))
print('O último nome desta pessoa é {}.'.format(nome[n-1]))