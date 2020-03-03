# If we have multiple super classes then who's init will be called

class A:
    def __init__(self):
        print("class A's init")

class B:
    def __init__(self):
        print("class B's init")

class C:
    def __init__(self):
        print("class C's init")

class D(A,B,C):
    pass


d = D()
# So here in case of multiple inheritance, python will follow an order which is MRO
# So it will always select the leftmost Super Class


# ----------------------------------------------------------------------------------------------------------------------
# Changing thr order of inheritance

class E(C,B,A):
    pass


print()
e = E()
# So when we change the order A,B,C to C,B,A then C became leftmost Super Class.


# ----------------------------------------------------------------------------------------------------------------------
# When LeftMost class does not have explicit __init__ method


class A:
    pass

class B:
    def __init__(self):
        print("class B's init")

class C:
    def __init__(self):
        print("class C's init")

class D(A,B,C):
    pass


print()
d2 = D()