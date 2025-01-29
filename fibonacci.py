N = int(input("Enter a number N : "))

a, b = 0, 1

for i in range(N):
    print(a)
    a, b = b, a + b
