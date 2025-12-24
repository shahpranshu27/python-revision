class A:
    a = 1

class B(A):
    b = 2

class C(B):
    c = 3

o = A()
print(o.a)  # prints 1
# print(o.b) # AttributeError: 'A' object has no attribute 'b'

p = B()
print(p.a, p.b)
# print(p.c)  # AttributeError: 'B' object has no attribute 'c'

q = C()
print(q.a, q.b, q.c)