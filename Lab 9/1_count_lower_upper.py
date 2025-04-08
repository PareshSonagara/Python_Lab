
def count_lower_upper(s):
    return {'lower': sum(1 for c in s if c.islower()), 'upper': sum(1 for c in s if c.isupper())}


print(count_lower_upper("Hello World! Python3"))
