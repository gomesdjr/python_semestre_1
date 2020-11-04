# Diego Gomes
# RA: 1904172

# String a ser lida
s = str(input())

# Sequencia de números
i1 = int(input())
f1 = int(input())
i2 = int(input())
f2 = int(input())

# Calculo do fatiamento
s1 = s[i1: f1 + 1]
s2 = s[i2: f2 + 1]

# Concatenação
print(s1 + s2)
