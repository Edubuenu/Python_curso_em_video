def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m².')

print('Controle de Terrenos')
print(25 *'-')
lar = float(input('Largura (m): '))
alt = float(input('Comprimento (m):'))
area(lar, alt)

