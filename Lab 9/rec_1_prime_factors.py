
def prime_factors(n, i=2):
    if i > n // 2:
        return [n] if n > 1 else []
    if n % i == 0:
        return [i] + prime_factors(n // i, i)
    return prime_factors(n, i+1)

print(prime_factors(100))
