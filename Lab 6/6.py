original_tuple = (1, 2, 3, 4, 5)
temp_list = list(original_tuple)  
temp_list[2] = 10              
new_tuple = tuple(temp_list)      
print(new_tuple)