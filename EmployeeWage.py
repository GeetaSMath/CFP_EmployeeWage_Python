"""Welcome to solve employee wage problem"""
# imported random function
#---UserCase one---
# employee Attendance
import random

# created employeecheck variable
# checking employee present or absent by using random function
# using if condition finding employee present or absent
employeeCheck = random.randrange(0, 2)
if employeeCheck == 0:
    print("employee is present")
else:
    print("employee is absent")

