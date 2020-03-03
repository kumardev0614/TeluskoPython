# Here we will see what is inheritance and how it works?
# Suppose we have a class A with some features and we are going to make a new class B with new features but we also
# need features of class A in class B.
# In that case we need inheritance where class B will inherit class A and access all the features of class A in class B
# This is called Single level inheritance


class A:                            # Here A is Super Class

    @classmethod
    def f1(cls):
        print('feature 1 called from class:', cls)

    @classmethod
    def f2(cls):
        print('feature 2 called from class:', cls)


class B(A):                         # Inheritance taking place, syntax "class subClass(SuperClass):"

    @classmethod
    def f3(cls):
        print('feature 3 called from class:', cls)

    @classmethod
    def f4(cls):
        print('feature 4 called from class:', cls)


a = A()
a.f1()
a.f2()


print()
b = B()                             # Because of inheritance b object can access both methods of Class A
b.f1()
b.f2()
b.f3()
b.f4()
