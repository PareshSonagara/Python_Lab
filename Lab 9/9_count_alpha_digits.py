
def count_alpha_digits(s):
    return {'alphabets': sum(c.isalpha() for c in s), 'digits': sum(c.isdigit() for c in s)}

print(count_alpha_digits("abc123xyz456"))
