'''
Class Method
A class method is a method that is bound to the class and not the instance of the class. It can modify a class state that applies across all instances of the class. Class methods are defined using the @classmethod decorator and take cls as the first parameter, which refers to the class itself.
'''

class Employee:
    
    a = 1 # Class attribute
    
    # Class Method displays class attribute and not instance attribute
    @classmethod
    def show(cls):
        print(f"The class attribute is: {cls.a}")

emp1 = Employee()
emp1.a = 5 # Instance attribute
emp1.show()