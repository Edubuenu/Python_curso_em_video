from math import sqrt
cateto_oposto = float(input('Digite o valor do cateto oposto:'))
cateto_adjacente = float(input('Digite o valor do cateto adjacente:'))
hipo = cateto_oposto**2 + cateto_adjacente**2

print('O valor da hipotenusa é: {:.2f}'.format(sqrt(hipo)))
