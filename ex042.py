
print('-=-'*20)
print('Analisador de Trângulos')
print('-=-'*20)
r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3< r1 + r2:
    print('Os segmento acima podem formar triângulo!')
    if r1 == r2 == r3:
        print('Forma um triângulo equilátero.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Forma um triângulo isósceles.')
    else:
        print('Forma um triângulo escaleno.')
else:
    print('Não formam triângulo')
print('-=-'*20)




