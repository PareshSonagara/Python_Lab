num = int(input("Enter a number: "))

if num < 0:
    num = -num

num_str = str(num)
digits = 0
for char in num_str:
    digits += 1

print("Number of digits:", digits)
