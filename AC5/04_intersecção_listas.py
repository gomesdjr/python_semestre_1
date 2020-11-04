# Escreva a funcao interseccao(lista1, lista2) abaixo:
def interseccao(lista1, lista2):
    inter = []  # Lista com elementos repetidos
    inter2 = []  # Lista sem elementos repetidos
    for n1 in lista1:  # Vai percorrer 1 elemento de inter e pular para inter2
        for n2 in lista2:  # Aqui vai percorrer cada elemento de inter2
            if n1 == n2:  # Aqui ele vai compara se são iguais, se for ele add
                inter.append(n1)

    for i in inter:  # Vai percorrer 1 elemento de inter e pular para inter2
        if i not in inter2:  # Caso o nº não esteja em inter 2 ele add
            inter2.append(i)
        inter2.sort()
    return inter2


# Programa principal
lista1 = eval(input('Informe a primeira lista de números: '))
lista2 = eval(input('Informe a segunda lista de números: '))
resultado = interseccao(lista1, lista2)
if isinstance(resultado, list):
    print('O resultado final é: ', resultado)
else:
    print("Erro. Voce deve devolver uma lista")
