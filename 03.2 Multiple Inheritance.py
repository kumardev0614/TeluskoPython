class A:
    @classmethod
    def f1(cls):
        print("F1 called by,", cls)


class B:
    @classmethod
    def f2(cls):
        print("F2 called by,", cls)


class C(A,B):                           # multiple inheritance subClass(SuperClass,Superclass)
    @classmethod
    def f3(cls):
        print("F3 called by,", cls)


a = A()
a.f1()

print()
b = B()
b.f2()

print()
c = C()
c.f1()
c.f2()
c.f3()
