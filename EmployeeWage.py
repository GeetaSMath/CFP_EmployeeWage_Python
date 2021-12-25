import random

Emp_Rate_Per_Hour = 20
FULL_TIME = 8
PART_TIME = 4
WORKING_HOURS = 100

Working_Days = 0
Total_Emp_Hour = 0

while Working_Days < 20 and Total_Emp_Hour <= WORKING_HOURS:
    Working_Days += 1
    emp_check = random.randrange(0, 3)

    # checking full-time, part-time or absent
    if emp_check == 0:
        emp_hour = FULL_TIME
    elif emp_check == 1:
        emp_hour = PART_TIME
    else:
        emp_hour = 0

    Total_Emp_Hour += emp_hour

    if Total_Emp_Hour > 100:
        Total_Emp_Hour -= emp_hour


# calculating monthly wage of employee
emp_wage = Emp_Rate_Per_Hour * Total_Emp_Hour
print(f"Monthly Wage of a Employee is :{emp_wage}")