# Crie um programa que faça o computador jogar Jokenpô com você.
import random

print('FAÇA SUA JOGADA')
print('[1] Pedra')
print('[2] Papel')
print('[3] Tesoura')
e = int(input('Digite sua escolha: '))
r = random.randint(1,3)

if e == 1 and r == 1:
    print('Você escolheu Pedra e a Máquina escolheu Pedra. Resultado: Empate')
elif e == 1 and r == 2:
    print('Você escolheu Pedra e a Máquina escolheu Papel. Resultado: Você perdeu')
elif e == 1 and r == 3:
    print('Você escolheu Pedra e a Máquina escolheu Tesoura. Resultado: Você venceu')
elif e == 2 and r == 2:
    print('Você escolheu Papel e a Máquina escolheu Papel. Resultado: Empate')
elif e == 2 and r == 3:
    print('Você escolheu Papel e a Máquina escolheu Tesoura. Resultado: Você perdeu')
elif e == 2 and r == 1:
    print('Você escolheu Papel e a Máquina escolheu Pedra. Resultado: Você venceu')
elif e == 3 and r == 3:
    print('Você escolheu Tesoura e a Máquina escolheu Tesoura. Resultado: Empate')
elif e == 3 and r == 1:
    print('Você escolheu Tesoura e a Máquina escolheu Pedra. Resultado: Você perdeu')
elif e == 3 and r == 2:
    print('Você escolheu Tesoura e a Máquina escolheu Papel. Resultado: Você venceu')
else:
    print('Número inválido')
