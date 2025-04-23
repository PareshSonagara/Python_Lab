import csv

data = [
    ['Roll No', 'Name', 'Subject1', 'Subject2', 'Subject3'],
    [101, 'Alice', 85, 90, 88],
    [102, 'Bob', 78, 82, 89],
    [103, 'Charlie', 92, 88, 91]
]

F = open('students.csv', 'w', newline='')
writer = csv.writer(F)
writer.writerows(data)
F.close()
