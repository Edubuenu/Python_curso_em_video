valor = list()
par = list()
impar = list()
while True:
    valor.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(valor):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print('=-'*30)
print(f'A lista completa é {valor}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')


    
