#Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite seu salário: R$ '))
percentual = 15
aumento = (salario * percentual) / 100
novo = aumento + salario
print('Seu salário com 15% de aumento é R$ {:.2f} '.format(novo))
