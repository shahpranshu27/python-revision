class Calculator:
    
    @staticmethod
    def greet():
        print("Welcome to the Calculator!")
    
    def square(self, x):
        print(f"square of {x} is {x*x}")
    
    def cube(self, x):
        print(f"cube of {x} is {x*x*x}")
    
    def square_root(self, x):
        print(f"square root of {x} is {x**0.5}")

calc1 = Calculator()
calc1.greet()
calc1.square(4)
calc1.cube(4)
calc1.square_root(16)