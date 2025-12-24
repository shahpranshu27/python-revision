class Employee:
    age = 30 # Class attribute
    salary = 50000
    
    def __init__(self, name, age, salary): # dunder method -> called automatically when an object is created
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute
        self.salary = salary  # Instance attribute
        print(f"Employee object is created")
    
    def getAge(self):
        print(f"Age is: {self.age}")
        
    @staticmethod
    def greet():
        print("Good Morning!")
        # self is not passed in this method as we don't need any instance specific data here. That's why we used @staticmethod decorator.

# john = Employee()
# john.name = "John Doe" # Instance attribute
# print(john.name, john.age, john.salary)

# Here, 'name' is an instance attribute and 'age' and 'salary' are class attributes as they directly belong to the class.

# mike = Employee()
# mike.name = "Mike Ross" # Instance attribute
# mike.age = 35 # Instance attribute
# print(mike.name, mike.age) # It will print 35, as instance attribute takes precedence over class attribute. If no instance attribute is found, it will look for class attribute.


# self keyword

# ross = Employee()
# ross.getAge() # This is under the hood -> Employee.getAge(ross), so 1 positional arguament is passed automatically, but in the getAge() method, we have not defined any parameter to accept it, so it will throw an error. That's why self is used to accept the instance automatically.

# Class attribute -> it is same for all instances of a class
# instance attribute -> it is unique for each instance of a class

# ross.greet()

joey = Employee("Joey Tribbiani", 33, 100000)
print(joey.name, joey.age, joey.salary)
print(f"Name: {joey.name},\nAge: {joey.age},\nSalary: {joey.salary}")