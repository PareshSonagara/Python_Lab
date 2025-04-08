gross_salary = float(input("Enter gross salary: "))
allowance = 0.10 * gross_salary
deduction = 0.03 * gross_salary
print("Net Salary:", gross_salary + allowance - deduction)