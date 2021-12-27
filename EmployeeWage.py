# imported random function
import random

# create Employee Class
class EmployeeWage:
    FULL_TIME = 8
    PART_TIME = 4

# created def function
    def employee_monthly_wage(self, compnay, emp_rate_per_hour, working_day, working_hours):
        """
            desc: calculating monthly wage of employee
            return: monthly wage
            passing parmaeters
        """
        working_days = 0
        total_emp_hour = 0
# checking employee condition for day comparring employee hours and total working hours
# passing three parameters
        while working_days < working_day and total_emp_hour <= working_hours:
            working_days += 1
            emp_check = random.randrange(0, 3)

            # checking full-time, part-time or absent
            emp_hour = self.calculate_emp_hours(emp_check)

            total_emp_hour += emp_hour

            if total_emp_hour > 100:
                total_emp_hour -= emp_hour
                break

        # calculating monthly wage of employee
        emp_wage = self.calculate_emp_wage(emp_rate_per_hour, total_emp_hour)
        print(f"Monthly Wage of a Employee is : {compnay} is : {emp_wage}")

    def calculate_emp_hours(self, emp_check):
        """
            desc: calculate daily hours of employee
            param: emp_check:
            return: employee hour
        """
        if emp_check == 0:
            return self.FULL_TIME
        elif emp_check == 1:
            return self.PART_TIME
        else:
            return 0

    def calculate_emp_wage(self, rate_per_hour, total_hour):
        """
            desc: calculating total employee wage
            return: employee wage
        """
        employee_wage = rate_per_hour * total_hour
        return employee_wage


if __name__ == '__main__':
    """
        Calling the calculate_monthly_wage function in EmployeeWage class
        to calculate monthly wage of employee.
    """
    emp_monthly_wage = EmployeeWage()
# passing value of the parametes to calculate monthly wage os employee

    emp_monthly_wage.employee_monthly_wage("DeepComputeSoft", 40, 50, 100)
    emp_monthly_wage.employee_monthly_wage("HP",40,60, 50)