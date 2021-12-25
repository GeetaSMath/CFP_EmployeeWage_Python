"""Welcome to solve employee wage problem"""
# imported random function
# ---UserCase three---
# employee Attendance
# employee monthly wage
import random

Emp_Rate_Per_Hour = 20
Full_Time = 8
Part_Time = 4

Emp_Check = random.randrange(0, 3)

# checking attendance
if Emp_Check == 0:
    Emp_Hour = Full_Time
elif Emp_Check == 1:
     Emp_Hour = Part_Time
else:
    Emp_Hour = 0

# calculating part time PartTime
emp_wage = Emp_Rate_Per_Hour * Emp_Hour
print(f"Monthly Employee Wage is :{emp_wage}")









