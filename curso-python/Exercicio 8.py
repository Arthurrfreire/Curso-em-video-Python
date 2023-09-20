#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

valor = int(input('Digite um valor em metros: '))
cem = valor * 100
mil = valor * 1000
print('O valor {} metros convertidos em centímetros é {} cm e convertido em milímetros é {} mm '.format(valor, cem, mil))
