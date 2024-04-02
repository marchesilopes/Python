# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
# deles e escrevendo o nome escolhido
import random

a1 = str(input('Digite o nome do aluno 1: '))
a2 = str(input('Digite o nome do aluno 2: '))
a3 = str(input('Digite o nome do aluno 3: '))
a4 = str(input('Digite o nome do aluno 4: '))

print('Os alunos são {}, {}, {} e {}. O escolhido para apagar o quadro é {}'. format(a1, a2, a3, a4, random.choice([a1, a2, a3, a4])))