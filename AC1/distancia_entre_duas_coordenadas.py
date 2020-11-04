import math

xa = float(input())
ya = float(input())
xb = float(input())
yb = float(input())

exp1 = (xb - xa) ** 2
exp2 = (yb - ya) ** 2

total = exp1 + exp2
dab = math.sqrt(total)

print(dab)
