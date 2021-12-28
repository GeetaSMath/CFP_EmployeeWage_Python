import random


class EmployeeWage:
    # constants
    FULL_TIME = 8
    PART_TIME = 4

    def __init__(self, company, emp_rate_per_hour, working_day, working_hours):
        self.company = company
        self.emp_rate_per_hour = emp_rate_per_hour
        self.working_day = working_day
        self.working_hours = working_hours

    def calculate_emp_hours(self, emp_check):
        """
            desc: calculate daily hours of employee
            param: emp_check:
            return: employee hour(int value)
        """
        if emp_check == 0:
            return self.FULL_TIME
        elif emp_check == 1:
            return self.PART_TIME
        else:
            return 0

    def employee_monthly_wage(self):
        """
            desc: calculating monthly wage of employee
            return: monthly wage
        """
        working_days = 0
        total_emp_hour = 0

        while working_days < self.working_day and total_emp_hour <= self.working_hours:
            working_days += 1
            emp_check = random.randrange(0, 3)

            # checking full-timme, part-time or absent
            emp_hour = self.calculate_emp_hours(emp_check)

            total_emp_hour += emp_hour

        # calculating monthly wage of employee
        emp_wage = self.calculate_emp_wage(self.emp_rate_per_hour, total_emp_hour)
        print(f"Monthly Wage of a Employee in a {self.company} is : {emp_wage}")
        return self.company, emp_wage

    def calculate_emp_wage(self, rate_per_hour, total_hour):
        """
            desc: calculating total employee wage
            param1: rate_per_hour:
            param2: total_hour:
            return: employee wage
        """
        employee_wage = rate_per_hour * total_hour
        return employee_wage

if __name__ == '__main__':
    """
        Calling the calculate_monthly_wage function in EmployeeWage class
        to calculate monthly wage of employee for multiple companies.
    """

    company_employee_wage_list = []

    DeepComputeSoft = EmployeeWage("DeepComputeSoft", 20, 20, 30)
    company_employee_wage_list.append(DeepComputeSoft.employee_monthly_wage())

    HP = EmployeeWage("HP", 30, 24, 50)
    company_employee_wage_list.append(HP.employee_monthly_wage())

    GSM = EmployeeWage("GSM", 30, 30, 50)
    company_employee_wage_list.append(GSM.employee_monthly_wage())

    for company_info in company_employee_wage_list:
       print(company_info)


    def get_total_wage_by_company():
        """
            desc: retrieve the total wage for a particular company from the list
            return: total wage
        """
        company_name = input("Enter the company name : ")
        flag = False
        for company in company_employee_wage_list:
            if company_name == company[0]:
                print("Monthly salary : " + str(company[1]))
                flag = True
                break
            if flag == False:
                print("Company is not there in the list.")

            get_total_wage_by_company()
