n1 = int(input('Digite o valor:'))
n2 = int(input('Outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(' A soma é {}, \n o produto é {} \n e a divisão é {:.3f}'.format(s, m, d), end='')
print('\n Divisão inteira {} e potência {}'.format(di, e))
