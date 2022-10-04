n1 = float(input('Insira a primeira nota:'))
n2 = float(input('Insira a segunda nota:'))
media = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, media))
if 7 > media >= 5:
    print('Está de recuperação')
elif media < 5:
    print('Está reprovado')
elif media > 7:
    print('Está aprovado')

