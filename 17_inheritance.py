# Parent Class
class Employee():
    company = "Google"
    
    def __init__(self, name, language):
        self.name = name
        self.language = language
    
    def show(self):
        print(f"The name of employee is {self.name} and he works in {self.company}")

# Child Class/Inherited Class
class Programmer(Employee):
    company = "Microsoft"
    
    def showLanguage(self):
        print(f"The name of programming language is {self.language}")

a = Employee("Harry", "Python")
b = Programmer("Rohan", "C++")

print(a.company, b.company)
b.show()