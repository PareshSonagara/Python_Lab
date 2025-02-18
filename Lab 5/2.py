import random

listt = []
indeces = []

n= int(input("Enter an interger : "))

for i in range(0,20):
    temp = random.randint(0,10)
    listt.append(temp)
    if temp == n:
        indeces.append(i)

print(listt)
print(indeces)