'''Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem, cobrando R$ 0,50 por KM para viagens até 200km e R$0,45 para viagens mais longas'''

distancia = float(input('Digite em KM a distância da sua viagem: '))
if distancia <= 200:
    preço = 0.50 * distancia
    print('O preço da sua passagem para {:.2f}km é de R$ {:.2f}'.format(distancia, preço))
else:
    preço = 0.45 * distancia
    print('O preço da sua passagem para {:.2f}km é de R$ {:.2f}'.format(distancia, preço))

'''
distancia = float(input('Qual é a distância da sua viagem?' ))
print('Você está prestes a começar uma viagem de {}Km.'.format(distância))
preço = distancia * 0.50 if distância <= 200 else distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))
'''