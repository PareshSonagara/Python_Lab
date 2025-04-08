
def frequency(s):
    words = s.split()
    freq = {word: words.count(word) for word in set(words)}
    return dict(sorted(freq.items()))

print(frequency("this is a test this is only a test"))
