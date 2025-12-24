class Employee:
    salary = 1000
    increment = 20
    
    @property
    def salaryAfterIncrement(self):
        return self.salary + (self.salary * self.increment) / 100
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary/self.salary) - 1) * 100

emp1 = Employee()
emp1.salaryAfterIncrement = 1500
print(f"Salary after increment is: {emp1.salaryAfterIncrement}")
print(f"New increment percentage is: {emp1.increment}")