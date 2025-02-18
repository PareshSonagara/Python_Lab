names = [("Aarav", "Rahul"), "Priya", ("Vikram", "Arjun"), "Ananya", "Sanya"]
boys = 0
girls = 0
for ele in names:
    if isinstance(ele, tuple):
        boys += len(ele)
    else:
        girls += 1
print("Number of boys:", boys)
print("Number of girls:", girls)
