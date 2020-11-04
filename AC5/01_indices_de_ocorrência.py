# Função
def todos_os_indices(seq, x):
    lista = []
    for i, e in enumerate(seq):
        if(e == x):
            lista.append(i)
    return lista


# Programa principal
sequencia = eval(input('Insira uma lista, tupla ou sting: '))
valor = eval(input('Informa o item a ser checado: '))
resultado = todos_os_indices(sequencia, valor)
if isinstance(resultado, list):
    if len(resultado) > 0:
        for item in resultado:
            print(f'O item {valor} aparece na posição {item}')
    else:
        print('lista vazia')
else:
    print('Erro. Voce deve devolver uma lista')
