#Um professor que sortear um dos seus alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random
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
    print('Nenhum aluno foi inserido. Encerrando o programa.') 
