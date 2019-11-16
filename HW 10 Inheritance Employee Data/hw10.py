"""
This program prompts the user to enter data for each employee, stores the data
in an object and then uses accessor methods to show production bonus along with
all data.
Author: Naveed Hussain
"""

# Employee Class (Parent)
class Employee(object):

    # Constructor for Employee class:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        
    # Set Name
    def set_name(self,name):
        self.name = name
        
    # Set Number
    def set_number(self, number):
        self.number = number
        
    # Get Name
    def get_name(self):
        return self.name
    
    # Get Number
    def get_number(self):
        return self.number

# Shift Supervisor Class (Child)
class ShiftSupervisor(Employee):

    # Constructor for Supervisor class:
    def __init__(self, name, number, annual_salary, goals, bonus):
        Employee.__init__(self, name, number)
        self.annual_salary = annual_salary
        self.goals = goals
        self.bonus = bonus

    # Set Annual Salary
    def set_annual_salary(self, annual_salary):
        self.annual_salary = annual_salary

    # Set Goals Met
    def set_goals(self, goals):
        self.goals = goals

    # Set Bonus
    def set_bonus(self, bonus):
        self.bonus = bonus

    # Get Annual Salary
    def get_annual_salary(self):
        return self.annual_salary
    
    # Get Goal Met
    def get_goals(self):
        return self.goals
    
    # Get Bonus
    def get_bonus(self):
        return self.bonus


def main():

    # Input Employee Details
    print("Please enter employee details below:")
    name = input("Name: ")
    number = input("Employee Number: ")
    annual_salary = input("Annual Salary: ")
    goals = input("Production Goals Met? Y/N: ")


    new_employee = ShiftSupervisor(name, number, annual_salary, goals, bonus=5000)
    
    # Output Employee Details
    print("\nEmployee Details:")
    print("Employee Name: ",new_employee.get_name())
    print("Employee Number: ",new_employee.get_number())
    print("Annual Salary: $", new_employee.get_annual_salary())

    # Give Bonus based on whether Production Goals were met 
    if goals == "Y":
        print("Production Goals met. Employee receives $", new_employee.get_bonus(), "bonus.")
        print()

    elif goals == "N":
        print("No Bonus received.")
        print()

    else:
        print("Bonus could not be calculated, please restart and re-enter Production Goals Met")
        print()   
main()
    

    
