from datetime import date
atual = date.today().year
ano = int(input('Insira o ano em que você nasceu:'))
alistar = atual - ano
conta = alistar - 18
con = 18 - alistar
if alistar < 18:
    print('Ainda vai se alistar daqui a {} anos'.format(con))
elif alistar == 18:
    print('Já é hora de se alistar')
elif alistar > 18:
    print('Já passou da hora, era pra ter se aistado ha {} anos'.format(conta))
