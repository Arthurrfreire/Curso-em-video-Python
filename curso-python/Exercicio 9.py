#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

def tabuada(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
numero = int(input("Digite um número inteiro: "))
tabuada(numero)
