casa = int(input('Digite o valor da casa:'))
salario = int(input('Digite o seu salário liquido: '))
anos = int(input('Em quantos anos pretende pagar?'))
meses = anos * 12
mensal = int(casa / meses)
condicao = float(mensal / salario)
if condicao < 0.3 :
    print('Parabéns, seu financiamento foi aprovado! Obrigado por negociar conosco.')
else:
    print('Infelizmente não foi possível dar continuidade com seu financiamento. Tente novamente daqui uns meses.')
