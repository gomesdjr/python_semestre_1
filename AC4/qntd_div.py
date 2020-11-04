def checa_quantidade_divisores(n, qtd):
    checa_quantidade_divisores = False
    div = 1
    cont = 0

    while div <= n:
        if (n % div) == 0:
            print('{} É divisivel por: {}'.format(n,div))
            cont = cont + 1
        div = div + 1
    if (qtd == cont):
        checa_quantidade_divisores = True
    return checa_quantidade_divisores

n = int(input('Insira um número: '))
qtd = int(input('Insira a quantidade de divisores: '))
if checa_quantidade_divisores(n, qtd):  # se a funcao devolve True, entao...
    print(n, "possui", qtd, "divisores")
else:
    print(n, "nao possui", qtd, "divisores")
