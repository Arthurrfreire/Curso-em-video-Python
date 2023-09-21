#Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite seu salário: R$ '))
novo = salario + (salario * 15 / 100)
print('Seu salário com 15% de aumento é R$ {:.2f} '.format(novo))
