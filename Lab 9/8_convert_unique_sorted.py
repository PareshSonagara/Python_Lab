
def convert(s):
    words = sorted(set(s.split()))
    return ' '.join(words)

print(convert("apple banana apple orange banana"))
