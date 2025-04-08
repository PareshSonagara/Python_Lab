
def create_list(lst1, lst2):
    return list(set(lst1) & set(lst2))

print(create_list([1, 2, 3, 4], [3, 4, 5, 6]))
