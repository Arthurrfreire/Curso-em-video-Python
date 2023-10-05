'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.'''

casa = float(input('Qual o valor da casa: R$ '))
salario = float(input('Qual o seu salário: R$ '))
anos = int(input('Em quantos anos quer pagar? '))
meses = anos * 12
prestação = casa / meses
if prestação <= 0.3 * salario:
    print('O valor da prestação mensal é de {:.2f}'.format(prestação))
else:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa, anos , prestação))
print('Empréstimo NEGADO')
