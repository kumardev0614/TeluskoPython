# Here we will learn about Types of methods available in python

class student:
    school = 'Dev international school'             # school name is common for all students

    def __init__(self, m1,m2,m3):                   # marks of each student
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avrg(self):                                 # we use instance methods to manipulate instance data
        return (self.m1+self.m2+self.m3)/3

    @classmethod                                    # we use class methods to work with static data
    def get_school_name(self):
        return self.school

    @staticmethod                                   # we use static method when we dont have to work on any kind of data
    def about_us():
        print('This is an international school. We have started in 2025'
              ' blah blah blah')


subham = student(58,92,45)
sameer = student(96,91,85)

print('percentage of subham:', subham.avrg())
print('percentage of sameer:', sameer.avrg())

print('school name of subham:', subham.get_school_name())
print('school name of sameer:', sameer.get_school_name())

print()
print('About Their School')
student.about_us()