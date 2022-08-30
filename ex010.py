n = int(input('Quanto dinheiro você tem na carteira?:'))
d = n / 5.03
e = n / 5.04
l = n / 5.89
bit = n / 103270
eth = n / 7969
shib = n / 0.0000634
baby = n / 0.000000006246
print('Com R$ {:.2f} você pode comprar US$ {:.2f}'.format(n, d))
print('Com R$ {:.2f} você pode comprar € {:.2f}'.format(n, e))
print('Com R$ {:.2f} você pode comprar £ {:.2f}'.format(n, l))
print('Com R$ {:.2f} você pode comprar btc {:.5f}'.format(n, bit))
print('Com R$ {:.2f} você pode comprar eth {:.5f}'.format(n, eth))
print('Com R$ {:.2f} você pode comprar shib {:.5f}'.format(n, shib))
print('Com R$ {:.2f} você pode comprar babydoge {:.5f}'.format(n, baby))

