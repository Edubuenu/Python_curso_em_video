#Exercise Python 081: Create a program that will read multiple numbers and put in a list. After that, show:
#A) How many numbers have been typed.
#B) The list of values, ordered in a decreasing way.
#C) Whether or not the value 5 was entered and is not in the list.
valores = []
while True:
    valores.append(int(input('Digite um valor: '))) 
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('=-' * 30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print('=-' * 30)
print(f'Os valores em ordem decrescente são {valores}')
print('=-' * 30)
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
