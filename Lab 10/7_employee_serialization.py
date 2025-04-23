import pickle

emp = {
    'empcode': 101,
    'empname': 'Alice',
    'doj': '2023-04-01',
    'salary': 75000
}

f = open('employee.dat', 'wb')
pickle.dump(emp, f)
f.close()

f = open('employee.dat', 'rb')
emp_loaded = pickle.load(f)
f.close()

print(emp_loaded)
