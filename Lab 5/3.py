import random

arr = []

for i in range(0,50):
    temp = random.randint(1,30)
    arr.append(temp)

arr.sort()
newArr = set(arr)

print(arr)
print(newArr)
