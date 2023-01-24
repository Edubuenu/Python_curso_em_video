expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len (pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')


#a = list()
#b = list()
#cont1 = 0
#cont2 = 0
#c = str(input('Digite sua expressão: '))
#for i, v in enumerate(c):
#    if v in '(':
#        a.append(v)
#        cont1 += 1
#    elif v in ')':
#        b.append(v)
#        cont2 += 1
#if cont1 == cont2:
#    print('Sua expressão está correta!')
#else:
#    print('Sua expressão está incorreta!')
#print(a)
#print(b)
#print(cont1)
#print(cont2)
