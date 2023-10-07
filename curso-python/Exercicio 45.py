'''Crie um programa que faça o computador jogar JOKEMPÔ com você'''

import random

def jogar_jokenpo(escolha_usuario):
    opcoes = ['pedra', 'papel', 'tesoura']
    escolha_computador = random.choice(opcoes)
    
    print(f'Você escolheu: {escolha_usuario}')
    print(f'O computador escolheu: {escolha_computador}')

    if escolha_usuario == escolha_computador:
        return 'Empate!'
    elif (escolha_usuario == 'pedra' and escolha_computador == 'tesoura') or \
         (escolha_usuario == 'papel' and escolha_computador == 'pedra') or \
         (escolha_usuario == 'tesoura' and escolha_computador == 'papel'):
        return 'Você ganhou!'
    else:
        return 'Você perdeu.'
    
escolha_usuario = input("Escolha: pedra, papel ou tesoura? ").lower()

if escolha_usuario not in ['pedra', 'papel', 'tesoura']:
    print("Escolha inválida. Por favor, escolha entre pedra, papel ou tesoura.")
else:
    resultado = jogar_jokenpo(escolha_usuario)
    print(resultado)
