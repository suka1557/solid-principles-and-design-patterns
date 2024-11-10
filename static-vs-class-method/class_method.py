"""
Suppose you want to create a class that is used for Salary Calculation.
The salary is calculated as follows:
    Total Salary = Base Salary (based on Department) + Bonus (based on Experience)

Now in future, you want to change the Base Salary for a department.
You want to make the change once and make sure that it is reflected across all new Employees that are created afterwards.

In this scenario, making use of class method makes as you'll be able to update the base salary for a department once
and later this will get reflected across all new objects.
So basically, class method is useful when you want to update state variables in a class,
that are common across all objects of the class.

"""

class Employee:
    base_salaries = {
        'HR': 50000,
        'IT': 60000,
        'Finance': 70000
    }
    bonus_rate = 10000

    def __init__(self, name, department, experience):
        self.name = name
        self.department = department
        self.experience = experience

    @classmethod
    def update_base_salary(cls, department, new_base_salary):
        cls.base_salaries[department] = new_base_salary

    def calculate_total_salary(self):
        base_salary = self.base_salaries[self.department]
        bonus = self.experience * self.bonus_rate
        return base_salary + bonus
    
    def get_base_salary(self):
        return self.base_salaries[self.department]
    
# Actual usage
if __name__ == '__main__':
    emp1 = Employee('John', 'HR', 2)

    print('Total Salary for emp1:', emp1.calculate_total_salary())
    print('Base Salary for emp1:', emp1.get_base_salary())

    # Update base salary for HR department
    Employee.update_base_salary('HR', 100000)

    emp2 = Employee('Smith', 'HR', 1)
    print('Total Salary for emp2:', emp2.calculate_total_salary())
    print('Base Salary for emp2:', emp2.get_base_salary())

    # Update base salary for IT department
    Employee.update_base_salary('IT', 150000)

    emp3 = Employee('Harry', 'IT', 4)
    print('Total Salary for emp3:', emp3.calculate_total_salary())
    print('Base Salary for emp3:', emp3.get_base_salary())


    