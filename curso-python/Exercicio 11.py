#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessário para pintá-lo, sabendo que cada litro de tinta, pinta uma área de 2m².

altura = float(input('Digite a altura da parede em metros: '))
largura = float(input('Digite a largura da parede em metros: '))
area = altura * largura
tinta = area * 2
print('A parede de altura {} e largura {} tem uma igual a {}, sendo necessário {} litros de tinta para pinta=lá '.format(altura, largura, area, tinta))
