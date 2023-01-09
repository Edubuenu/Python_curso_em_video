n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opcao = int(input('\n Qual é a sua opção? '))
    print('\n')
    if opcao == 1:
        somar = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, somar))
    elif opcao == 2:
        produto = n1 * n2
        print('O resultado de {}x{} é {}'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os novos números: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao ==5:
        print('Finalizando...')
    else:
        print('\n Opção inválida')
    print('\n')
    print('=-=' * 10)
print('Fim do programa volte sempre!')
