'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%'''

salario = float(input('Digite o valor do seu salário: R$ '))
if salario > 1250.00:
    aumento = salario + 0.10 * salario
    print('Seu salário com aumento de 15% é de R$ {:.2f}'.format(aumento))
else:
    aumento = salario + 0.15 * salario
    print('Seu salário com 10% de aumento é de {:.2f}'.format(aumento))
