tuples_list = [(1, 2), (), (3, 4), (), (5, 6), ()]

list1 = []
for t in tuples_list:
    if t:  
        list1.append(t)
tuples_list=tuple(list1)
print(tuples_list)