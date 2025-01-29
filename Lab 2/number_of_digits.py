num = int(input("Enter a number: "))

if num < 0:
    num = -num

num_str = str(num)
digits = len(num_str)

print("Number of digits:", digits)
