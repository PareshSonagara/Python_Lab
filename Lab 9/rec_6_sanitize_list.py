
def sanitize(lst, i=0):
    if i == len(lst):
        return lst
    if lst[i] < 0:
        lst[i] = 0
    return sanitize(lst, i+1)

lst = [-1, 5, -3, 7, -2]
print(sanitize(lst))
