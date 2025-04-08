
def average(lst, i=0, total=0):
    if i == len(lst):
        return total / len(lst)
    return average(lst, i+1, total+lst[i])

print(average([10, 20, 30, 40]))
