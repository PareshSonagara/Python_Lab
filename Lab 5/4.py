import random

plusArr = []
minusArr = []

for i in range(0,30):
    n = random.randint(-10,5)
    if n < 0:
        minusArr.append(n)
    else:
        plusArr.append(n)

print(plusArr)
print(minusArr)
