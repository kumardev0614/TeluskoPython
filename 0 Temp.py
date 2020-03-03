class student:

    def __init__(self, math, eng):
        self.math = math
        self.eng = eng

    def __str__(self):  # real signature unknown
        values = '{} {}'.format(self.math, self.eng)
        return values
    pass


raju = student(88,99)

# Now we will overload __str__() method, but where this method is used

a = 99              # a is reference variable for int object and this int object is holding the value 99
print(a)
print(a.__str__()) # This object is returning value, hold by object we are passing

print(raju)        # But here we are getting object address, it should return values hold by object pointing by raju.
# so we will overload __str__() method so it will show values, not the address

print()
sham = student(55,66)
print("sham's marks:",sham)


class A:
    def sum(self,a = 0, b = 0, c = 0):
        return a+b+c

s1 = A()
print('sum =', s1.sum())
print()
