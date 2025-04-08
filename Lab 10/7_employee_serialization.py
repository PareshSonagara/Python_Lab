
import pickle

class Employee:
    def __init__(self, empcode, empname, doj, salary):
        self.empcode = empcode
        self.empname = empname
        self.doj = doj
        self.salary = salary

    def __repr__(self):
        return f"{self.empcode}, {self.empname}, {self.doj}, {self.salary}"

emp = Employee(101, 'Alice', '2023-04-01', 75000)

with open('employee.dat', 'wb') as f:
    pickle.dump(emp, f)

with open('employee.dat', 'rb') as f:
    emp_loaded = pickle.load(f)

print(emp_loaded)
