'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
A multa vai custar R$7,00 por cada KM acima do limite'''

v = float(input('Digite a velocidade do seu carro: '))
multa = (v - 80) * 7
if v <= 80:
    print('Seu carro estar dentro do limite permitido da via!') 
else:
    print('Seu carro ultrapassou o limite da via...')
    print('Você deverá pagar uma multa de R$ {:.2f} por essa infração'.format(multa))
