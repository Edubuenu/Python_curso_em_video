n = int(input('Digite um número inteiro para ser convertido:'))
base = int(input('Digite 1 para binário \nDigite 2 para octal \nDigite 3 para hexadecimal \nDigite 4 para todos anteriores:'))
if base == 1:
    print(n,'em binário fica:', bin(n))
elif base == 2:
    print(n,'em hexadecimal fica:', hex(n))
elif base == 3:
    print(n,'em octal fica:', oct(n))
elif base == 4:
    print(n,'em binário fica:', bin(n),'\n',n,'em hexadecimal fica:', hex(n),'\n',n,'em octal fica:',  oct(n))
