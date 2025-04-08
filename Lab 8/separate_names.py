names = {'Alice', 'Andrew', 'Bob', 'Bill', 'Amy', 'Brian'}
set_a = {name for name in names if name.startswith('A')}
set_b = {name for name in names if name.startswith('B')}
print("Names starting with A:", set_a)
print("Names starting with B:", set_b)