#Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o valor do produto: '))
desconto = preco * 0.05
novo = preco - desconto
print('O novo valor do produto com 5% de desconto é R$ {:.2f} '.format(novo))
