def Leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n

def Leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[031mERRO: por favor, digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse númewor.\033[m')
            return 0
        else:
            return n

n1 = Leiaint('Digite um Inteiro: ')
n2 = Leiafloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')