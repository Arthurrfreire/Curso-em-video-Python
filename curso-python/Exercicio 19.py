#Um professor que sortear um dos seus alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

'''import random
alunos = []
while True:
    nome = input('Digite o nome do aluno (ou fim para encerrar): ')
    if nome.lower() == 'fim':
        break
    alunos.append(nome)
if alunos:
    escolhido = random.choice(alunos)
    print('O aluno escolhido para apagar o quadro é: {}'.format(escolhido))
else:
    print('Nenhum aluno foi inserido. Encerrando o programa.')'''

import random
n1 = str(input('Primeiro aluno:'))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
