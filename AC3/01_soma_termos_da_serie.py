# Aluno: Diego Junior Gomes
# RA: 1904172

n = int(input())
numerador = 1
soma = 0

for denominador in range(1, n + 1, 1):  # atribuição, condição, incremento
    denominador = (denominador ** 2)
    total = numerador / denominador
    soma = soma + total
print("{0:.6f}".format(soma))
