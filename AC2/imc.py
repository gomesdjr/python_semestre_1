def massa_c(imc):
    if imc < 17.0:
        print("Muito abaixo do peso")
    elif imc <= 17.0 or imc < 18.50:
        print("Abaixo do peso")
    elif imc <= 18.50 or imc < 25.00:
        print("Peso normal")
    elif imc <= 25.0 or imc < 30.00:
        print("Acima do peso")
    elif imc <= 30.0 or imc < 35.00:
        print("Obesidade grau I")
    elif imc <= 35.0 or imc < 40.00:
        print("Obesidade grau II")
    else:
        print("Obesidade grau III")


import math

altura = float(input())
peso = float(input())
imc = peso / (altura * altura)
imc = round(imc, 2)  # função round (Não precisa usar math.round)
print('{}'.format(imc))

massa_c(imc)
