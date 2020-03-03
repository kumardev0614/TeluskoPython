# Her we will see how constructor works in case of inheritance


# case 1) When init is defined only in Super Class
class A:
    def __init__(self):
        print("class A's init")


class B(A):
    pass


a = A()

# Here When you create an object of class B. python will find init for Class B.
# if it is not found, then it will call init of super class A.
b = B()


# ----------------------------------------------------------------------------------------------------------------------
# case 2) When init is defined in sub Class.

class C:
    def __init__(self):
        print("class C's init")


class D(C):
    def __init__(self):  # Here init of class will be get found and init of B will be run
        print("class D's init")


print()
d = D()


# ----------------------------------------------------------------------------------------------------------------------
# case 3) When we need init of both Super and Sub Class

class E:
    def __init__(self):
        print("class E's init")


class F(E):
    def __init__(self):
        super().__init__()  # To call init of Super class
        print("class F's init")


print()
f = F()


# ----------------------------------------------------------------------------------------------------------------------
# Because __init__() is a method, so all these concepts also apply on the all type of methods in the class.
# Ex

class G:
    def __init__(self):
        print("class G's init")

    def g_method(self):
        print("g_method is called")


class H(G):
    def __init__(self):
        super().__init__()  # To call init of Super class
        print("class H's init")

    def g_method(self):
        super().g_method()
        print("g_method is called from H")


print()
h = H()
h.g_method()
