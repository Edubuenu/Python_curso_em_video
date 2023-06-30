def aumentar(preço = 0, taxa = 0, formato=False):
    """
    -> Calcula o  aumento de um determinado preço.
    :param preço: o preço que se quer reajustar
    :param taxa: qual é a porcentagem do aumento.
    :paramformato: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formato.
    """


    res =preço+(preço*taxa/100)
    return res if formato is False else moeda2(res)



def diminuir(preço = 0 , taxa = 0, formato = False):
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda2(res)

def dobro(preço = 0):
    res = preço * 2
    return res if formato is False else moeda2(res)

def metade(preço = 0, formato = False):
    res = preço / 2
    return res if formato is False else moeda2(res)


def moeda2(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')

def resumo(preço=0, taxaa=10, taxar=5 ):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: {moeda2(preço)}')