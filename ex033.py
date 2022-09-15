a = int(input('Digite um primeiro valor:'))
b = int(input('Digite um segundo valor:'))
c = int(input('Digite um terceiro valor:'))
#menor
if a<b and a<c:
    menor = a
if b<c and b<a:
    menor = b
if c<b and c<a:
    menor = c
#maior
if a>b and a>c:
    maior = a
if b>c and b>a:
    maior = b
if c>b and c>a:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))

    
