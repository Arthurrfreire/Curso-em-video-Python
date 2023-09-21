#Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por KM rodado.

dias = float(input('Quantos dias alugados? '))
km = float(input('Quantos KM rodados? '))
carro = dias * 60
rota = km * 0.15
pagar = carro + rota
print('O total a pagar é de R$ {:.2f} '.format(pagar))
