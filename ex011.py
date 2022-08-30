l = int(input('Qual a largura da parede?'))
a = int(input('Qual a altura da parede?'))
area = l * a
tinta = area / 2
print('É necessário {} litros de tinta para pintar {}m²'.format(tinta, area))
