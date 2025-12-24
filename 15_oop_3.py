class Demo:
    a = 4  # Class variable

o = Demo()
print(o.a) # prints class attribute as there is no instance attribute 'a' yet
o.a = 0 # Instance variable
print(o.a) # prints instance attribute
print(Demo.a) # prints class attribute as it is accessed using class name

# So, the class variable is not changed, because when we did o.a = 0, a new instance variable 'a' is created for the object 'o' which shadows the class variable 'a'.
# So, instance variable is changed, but class variable remains the same.