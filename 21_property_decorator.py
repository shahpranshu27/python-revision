
'''
Property decorators in python provide a way to manage attribute access in classes by defining getter, setter, and deleter methods using the @property decorator. This allows for controlled access to private attributes while maintaining a clean and intuitive interface.
it is same as using getter and setter methods, but with a more pythonic syntax.
there's no difference in functionality between using property decorators and traditional getter/setter methods; both approaches achieve the same goal of encapsulating attribute access.
'''

# class Person:
#     def __init__(self, age):
#         self._age = age
    
#     def get_age(self):
#         return self._age
    
#     def set_age(self, value):
#         if value < 0:
#             print("Age can't be negative!")
#         else:
#             self._age = value

# # Using it:
# person = Person(25)
# print(person.get_age())  # 25
# person.set_age(30)       # 30
# print(person.get_age())  # 30
# person.set_age(-5)       # Doesn't work

class Person:
    def __init__(self, age):
        self._age = age
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 0:
            print("Age can't be negative!")
        else:
            self._age = value

# Their code still works the same!
person = Person(25)
print(person.age)  # 25
person.age = 30  # Still looks like a variable
print(person.age)  # 30
person.age = -5  # Doesn't work