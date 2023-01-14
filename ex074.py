#Exercise Python 074: Create a program that will generate five random numbers and put in a tuple. After that, show the listing of generated numbers and also indicate the smallest and highest value that are in the tuple.
from random import randint
while True:
    lista = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
    print(f'Os números sorteados foram: {lista}')
    print(f'O maior número foi: {max(lista)}')
    print(f'O menor número foi: {min(lista)}')
    resp = str(input('Sortear de novo? [S/N}')).strip().upper()[0]
    if resp == 'N':
        
        break
