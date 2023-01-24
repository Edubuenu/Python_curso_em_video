#Exercise Python 079: Create a program where the user can type multiple numeric values and register
#them in a list. If the number already exists inside, it will not be added. At the end, all the
#unique values entered will be displayed, in ascending order.
valor = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in valor:
        valor.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('=-' * 30)
print(f'Os valores digitados foram {valor}')
