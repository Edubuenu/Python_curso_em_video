print('=-='*30)
print('VAMOS JOGAR PAR OU IMPAR?')
print('=-='*30)
from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou impar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 ==1:
            print('VocÊ venceu!')
            v += 1
        else:
            print('você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'Game over! Você venceu {v} vezes.')
