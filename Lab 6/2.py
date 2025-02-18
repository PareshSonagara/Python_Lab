students = [(1, "Aarav", 20), (2, "Priya", 21), (3, "Vikram", 22)]
roll_no = []
names = []
ages = []
for student in students:
    roll_no.append(student[0])
    names.append(student[1])
    ages.append(student[2])
print("Roll Numbers:", roll_no)
print("Names:", names)
print("Ages:", ages)
