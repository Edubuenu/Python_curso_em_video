from random import randint
from time import sleep
computador = randint(0,5)# faz o computador pensar
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei?')) #jogador tenta adivinhar
print('PROCESSANDO')
sleep(2)
if jogador == computador :
    print('PARABENS! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no numero {} e não no {}!'.format(computador, jogador))
