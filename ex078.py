#Python Exercise 078: Make a program that reads 5 numeric values and saves them in a list.
#At the end, show what was the highest and lowest value typed and their respective positions
#in the list.
valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(f'Os números digitados foram {valores}')
print(f'O maior número digitado foi {max(valores)} e está na posição ', end='')
for i, v in enumerate(valores):
    if v == max(valores):
        print(f'{i}...', end='')
print(f'\nO menor número digitado foi {min(valores)} e está na posição ', end='')
for i, v in enumerate(valores):
    if v == min(valores):
        print(f'{i}...', end='')
