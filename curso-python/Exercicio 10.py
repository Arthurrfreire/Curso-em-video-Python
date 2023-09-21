#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. Considere US$ = R$ 3,27

dinheiro = float(input('Quanto dinheiro você tem na carteira? R$ '))
print('Com o dinheiro informado é possivel comprar US$ {:.2f}'.format(dinheiro / 3.27))
