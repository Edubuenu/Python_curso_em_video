import time
def contador(i, f, p):
    print('-=' * 25)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i<f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            cont += p
            time.sleep(0.5)
        print('FIM!')      
    else:
        cont = i
        while cont >= f:
           print(f'{cont} ', end='')
           cont -= p
           time.sleep(0.5)
        print('FIM!') 

contador(1, 10 , 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(ini, fim, passo)

