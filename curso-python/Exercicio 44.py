'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamentos:

- A vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros'''

produto = float(input('Digite o valor do produto: R$ '))
pagamento = int(input('''Selecione a opção:
                      [ 1 ] Dinheiro ou cheque
                      [ 2 ] À vista no cartão
                      [ 3 ] Dividido em 2x no cartão
                      [ 4 ] Dividido em 3x ou mais no cartão
                      Sua opção: '''))
if pagamento == 1:
     preço = produto * 0.1
     desconto = produto - preço
     print('O valor a pagar é R${:.2f} com 10% de desconto'.format(desconto))
elif pagamento == 2:
     preço = produto * 0.05
     desconto = produto - preço
     print('O valor a pagar é R${:.2f} com 5% de desconto'.format(desconto))
elif pagamento == 3:
     parcelado = produto / 2
     print('O valor a pagar é R${:.2f} em duas parcelas de {:.2f}'.format(produto, parcelado))
elif pagamento == 4:
     juros = produto * 0.2
     aumento = produto + juros
     print('O valor a pagar é R${:.2f} com 20% de juros'.format(aumento))
