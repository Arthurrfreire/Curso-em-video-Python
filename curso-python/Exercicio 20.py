#O mesmoo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada.

'''import random
alunos = []
for i in range(4):
    nome = input(f'Digite o nome do {i+1}º aluno: ')
    alunos.append(nome)
random.shuffle(alunos)
print('\nOrdem de apresentação dos trabalhos: ')
for i, aluno in enumerate(alunos, start=1):
    print(f'{i}. {aluno}')'''
    
from random import shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será ')
print(lista)
