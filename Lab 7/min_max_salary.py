employees = {1: {'roll_no': 101, 'salary': 50000}, 
             2: {'roll_no': 102, 'salary': 60000}, 
             1: {'roll_no': 103, 'salary': 45000}, 
             2: {'roll_no': 104, 'salary': 75000}}

departments = {}
for dept, data in employees.items():
    if dept not in departments:
        departments[dept] = []
    departments[dept].append(data['salary'])

for dept, salaries in departments.items():
    print(f"Department {dept}: Min Salary = {min(salaries)}, Max Salary = {max(salaries)}")