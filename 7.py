original_tuple = (1, 2, 3, 4, 5)
element_to_remove = 3
new_tuple = tuple(x for x in original_tuple if x != element_to_remove)
print(new_tuple)