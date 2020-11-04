# Escreva a funcao media_pares_impares(lista) abaixo:
def media_pares_impares(lista):
    pares = []
    impares = []
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    print(sum(pares) / len(pares))
    print(sum(impares) / len(impares))

# Programa principal (ja implementado, voce nao precisa se preocupar com o codigo partir deste ponto)
lista = eval(input())
media_pares_impares(lista)