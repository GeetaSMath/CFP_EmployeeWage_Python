"""Welcome to solve employee wage problem"""
# imported random function
# ---UserCase three---
# employee Attendance
# employee monthly wage
import random

Emp_Rate_Per_Hour = 20
Full_Time = 8
Part_Time = 4

Working_Days = 20
total_Emp_Hour = 0

for day in range(1, Working_Days + 1):
    Emp_Check = random.randrange(0, 3)

    # checking attendance
    if Emp_Check == 0:
        Emp_Hour = Full_Time
    elif Emp_Check == 1:
        Emp_Hour = Part_Time
    else:
       Emp_Hour = 0

    total_Emp_Hour += Emp_Hour

# calculating part time PartTime
emp_wage = Emp_Rate_Per_Hour * total_Emp_Hour
print(f"Monthly Employee Wage is :{emp_wage}")
