
import string

def ispangram(s):
    return set(string.ascii_lowercase) <= set(s.lower())


print(ispangram("The quick brown fox jumps over the lazy dog"))
