# Here we will see multilevel inheritance


class A:
    @classmethod
    def f1(cls):
        print("F1 called by,", cls)


class B(A):
    @classmethod
    def f2(cls):
        print("F2 called by,", cls)


class C(B):
    @classmethod
    def f3(cls):
        print("F3 called by,", cls)


a = A()
a.f1()
# a.f2()        AttributeError: 'A' object has no attribute 'f2'

print()
b = B()
b.f1()
b.f2()
# b.f3()          AttributeError: 'B' object has no attribute 'f3'

print()
c = C()
c.f1()
c.f2()
c.f3()