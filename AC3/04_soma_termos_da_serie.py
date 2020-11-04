n = int(input())
incremento = 0
numerador = 1
soma = 0
contagem = 1

while contagem <= n:
    incremento = incremento + 1  # incremento recebe 0 e vai somando 1 unidade para ser elevado ao quadrado
    denominador = incremento ** 2  # razão aritimética, o valor do incremento sempre será elevado a 2
    total = numerador / denominador  # numerado será sempre 1, logo 1 sempre irá divdir
    soma = (total + soma)  # a divisão da fração é armazenada em soma e seu valor é somado com o total
    contagem = contagem + 1  # a contagem vai receber 1 e acrescentar 1, o programa será executado enquanto ela for
    # menor que o número inserido pelo usuário
print("{0:.6f}".format(soma))
