# Here we will see what is operator overloading.
# We have many operators like +, -, *, **, <, >= etc....
# For every operator in python there is a pre defined special method.
# Ex - __add__, __sub__, __mul__ etc. Also these methods are defined differently for different class.
# like 5 + 5, __add__ is defined in int class, for '5' + '5' __add__ is defined differently in str class.
# print(5+6) is equal to print(int.__add__(5,6))

print(5+6)
print(int.__add__(5,6))

print()
print('h' + 'i')
print(str.__add__('h','i'))

# So here we have our own class student and we want to use + between two objects of class student
# But __add__ for student is not defined we have to define it by our self.
# So We will overload + operator by defining __add__ method for our own class


class student:
    def __init__(self, math, eng):
        self.math = math
        self.eng = eng

    def __add__(self, other):
        total1 = self.math + self.eng       # 92 + 89 = 181
        total2 = other.math + other.eng     # 69 + 45 = 114
        return total1 + total2 # 295        # here total1 and total2 are of int type so it's addition is predefined

    def __gt__(self, other):                # __gt__ is used for > Greater Than operator
        total1 = self.math + self.eng
        total2 = other.math + other.eng
        if total1 > total2:                 # Here calling int.__gt__(total1, total2) which is predefined for int class
            return True
        else:
            return False




raju = student(92,89)
sham = student(69,45)

sita = student('hi ', 'how ')
tina = student('are ', 'you')

print(raju + sham) # In this case int.__add__(total1,total2) will be called in last
print(sita + tina) # In this case str.__add__(total1,total2) will be called in last

if raju > sham:
    print("Raju has greater marks in total")
else:
    print("Sham has greater marks in total")

