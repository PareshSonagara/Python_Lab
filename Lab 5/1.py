import random

odd = []
even = []

for i in range(0,5):
    temp = random.randint(1,100)
    if temp%2 == 0:
        temp = temp + 1
    odd.append(temp)

for i in range(0,4):
    temp = random.randint(1,100)
    if temp%2 != 0:
        temp = temp + 1
    even.append(temp)

odd[2] = even

print(odd)