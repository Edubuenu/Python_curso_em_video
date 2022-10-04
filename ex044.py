print('{:=^40}'.format(' LOJA '))
valor = float(input('Insira o valor do produto:'))
pagar = int(input('Qual forma de pagamento?\n1-Dinheiro/cheque\n2-á vista no cartão\n3-2x no cartão\n4-3x ou mais no cartão'))
avista = valor
if pagar == 1:
    total = valor - (valor * 10 / 100)
    print('Você teve 10% de desconto, ficando o total a pagar de R${:.2f}'.format(total))
elif pagar == 2:
    total = valor - (valor * 5 / 100)
elif pagar == 3:
    total = valor
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif pagar == 4:
    total = valor + (valor * 20 / 100)
    totalparce = int(input('Quantas parcelas?'))
    parcela = total / totalparce
    print('Sua compra será parcelada em {}x de R${:.2f}'.format(totalparce, parcela))
else:
    print('Opção inválida.')
print('Sua compra de R$ {:.2f} vai custar R${:.2f} no final.'.format(valor, total))
