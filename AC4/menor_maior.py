def le_e_devolve_menor():
    n = int(input('Insira o primeiro número: '))
    menor = n
    if n < 0:
        menor = 0
    while n >= 0:
        if n < menor:
            menor = n
        n = int(input('Insira um número positivo ou -1 para finalizar: '))
    return menor


def le_e_devolve_maior():
    n = int(input('Insira o primeiro número: '))
    maior = n
    if n < 0:
        maior = 0
    while n >= 0:
        if n > maior:
            maior = n
        n = int(input('Insira um número positivo ou -1 para finalizar: '))
    return maior


# Programa principal (ja implementado, voce nao precisa se preocupar com o codigo a partir deste ponto)
opcao = input('Escolha menor ou maior: ')
if opcao == 'menor':
    menor = le_e_devolve_menor()
    print('O menor número é: {}'.format(menor))
elif opcao == 'maior':
    maior = le_e_devolve_maior()
    print('O maior número é: {}'.format(maior))

