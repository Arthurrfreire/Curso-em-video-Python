#Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço = float(input('Digite o valor do produto: R$ '))
novo = preço - (preço * 0.05)
print('O novo valor do produto com 5% de desconto é R$ {:.2f} '.format(novo))
