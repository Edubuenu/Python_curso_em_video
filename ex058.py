from random import randint
computador = randint(0, 10)
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.\nSerá que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    palpite = int(input('Qual é seu palpite? '))
    palpites += 1
    if palpite == computador:
        acertou = True
    else:
        if palpite < computador:
            print('Mais... Tente mais uma vez. ')
        if palpite > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
