import math

angulo = float(input())
velocidade = float(input())
gravidade = float(input())

seno = math.radians(angulo)
angulo2 = math.sin(seno)

altura = (((velocidade ** 2) * (angulo2 ** 2)) / (gravidade * 2))
print(altura)
