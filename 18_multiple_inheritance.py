'''
Multiple Inheritance
When a class is derived from more than one base class it is called multiple inheritance.
The derived class inherits all the features of the base case.
'''

# Parent Class
class Employee():
    company = "Google"
    
    def __init__(self, name, language):
        self.name = name
        self.language = language
    
    def show(self):
        print(f"The name of employee is {self.name} and he works in {self.company}")

class Coder:
    company = "Facebook"
    
    def showCoder(self):
        print(f"The name of programming language is {self.language} and coder is working in {self.company}")

# Child Class/Inherited Class
class Programmer(Employee, Coder):
    company = "Microsoft"
    
    def showLanguage(self):
        print(f"The name of programming language is {self.language}")

a = Employee("Harry", "Python")
b = Programmer("Rohan", "C++")

print(a.company, b.company)
b.show()
b.showCoder()