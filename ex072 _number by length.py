#Python Exercise 72: Create a program that has a fully populated double with an extended count, from zero to twenty. Your program should read a number over the keyboard (between 0 and 20) and show it in full.
cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'desessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        num = int(input('Digite um número entre 0 e 20 para vê-lo por extenso:'))
        if 0 <= num <= 20:
            break
        print('Número inválido. ', end='')
    print(f'Você digitou o número {cont[num]}')
    print('-' * 30)
    resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    print(resp)
    print('-' * 30)
    if resp == 'N':
        break
print('-' * 30)
print('Programa encerrado')

