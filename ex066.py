soma = count = 0
while True:
    num = int(input('Digite um valor [999 para parar]: '))
    if num == 999:
        break
    count += 1
    soma += num
print(f'A soma dos valores foi {soma} e foram inseridos {count} números!')


#n = 0
#soma = 0
#count = -1
#print('Digite 999 para parar!')
#while n != 999:
#    n = int(input('Digite um número: '))
#    count += 1
#    soma += n
#soma -= 999
#print('A soma dos valores foi {} e foram inseridos {} números'.format(soma, count))
