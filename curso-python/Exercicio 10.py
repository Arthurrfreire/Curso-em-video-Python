#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. Considere US$ = R$ 3,27

dinheiro = float(input('Digite quanto você tem em dinheiro agora: R$ '))
dolar = dinheiro / 3.27
print('Com o dinheiro informado é possivel comprar US$ {:.2f}'.format(dolar))
