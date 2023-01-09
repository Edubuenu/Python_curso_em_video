print('Gerador de PA')
print('-=' * 10)
n1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
termo = n1
count = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while count <= total:
        print('{} ->'.format(termo), end='')
        termo += r
        count += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termo(s) mostrados'.format(total))
print('FIM')
