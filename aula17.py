#num = [2, 3, 9, 1]
#num[2]= 104
#num.append(8)
#num.sort(reverse=True)
#num.insert(2, 2)
#if 2 in num:
#    num.remove(2)
#print(num)
#print(f'Essa lista tem {len(num)} elementos.')

#valores = []
#valores.append(5)
#valores.append(9)
#valores.append(4)
#for c, v in enumerate(valores):
#    print(f'Na posição {c} encontrei o valor {v}.')
#print(valores)

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
