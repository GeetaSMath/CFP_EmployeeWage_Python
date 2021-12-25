"""Welcome to solve employee wage problem"""
# imported random function
#---UserCase two---
# employee Attendance
import random

Emp_Rate_Per_Hour = 20
Full_Time = 8

Emp_Check = random.randrange(0, 2)

# checking attendance
if Emp_Check == 0:
    Emp_Hour = Full_Time
else:
    Emp_Hour = 0
# calculating employee wage
emp_wage = Emp_Rate_Per_Hour * Emp_Hour
print(f"Monthly Employee Wage is :{emp_wage}")




