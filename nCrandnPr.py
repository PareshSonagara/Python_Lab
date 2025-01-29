n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))

fact_n = 1
for i in range(1, n + 1):
    fact_n *= i

fact_r = 1
for i in range(1, r + 1):
    fact_r *= i

fact_n_r = 1
for i in range(1, n - r + 1):
    fact_n_r *= i

nCr = fact_n // (fact_r * fact_n_r)

nPr = fact_n // fact_n_r

print(n, "C", r, "=", nCr)
print(n, "P", r, "=", nPr)
