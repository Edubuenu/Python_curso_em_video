from datetime import date
atual = date.today().year
ano = int(input('Insira o ano de nascimento:'))
idade = atual - ano
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Vai competir como MIRIM.')
elif idade <= 14:
    print('Vai competir como INFANTIL.')
elif idade <= 19:
    print('Vai competir como JUNIOR.')
elif idade <= 25:
    print('Vai competir como SÊNIOR.')
elif idade > 25:
    print('Vai competir como MASTER.')
