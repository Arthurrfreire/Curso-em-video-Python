#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

valor = int(input('Digite um valor em metros: '))
print('O valor {} metros convertidos em centímetros é {:.0f} cm e convertido em milímetros é {:.0f} mm '.format(valor, (valor * 100), (valor * 1000)))
