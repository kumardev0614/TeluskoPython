# suppose we are making a program where we have to work on computers. But we don't have anything like computers in
# python, we have integer objects, list objects, sets but we don't have computer objects.
# So in this case we have build computer objects. To do so, first we have to create class named 'computer' which
# will define properties and behaviour of our computer objects.
# So we can say class is a blueprint of any object.


class Computer:                                         # that's how we define a class
    def __init__(self, name, cpu, ram):                 # commonly here we define properties of our objects
        self.name = name
        self.cpu = cpu
        self.ram = ram

    def process(self, input):                           # process is behavior of every computer, it takes input
        output = input + 15                             # then do something with it
        return output                                   # and generates output


# Now we can create computer objects

comp1 = Computer('lisa', 'i7', 16)                  # Object creation and initializing variables
comp2 = Computer('NoteBook4', 'i3', 4)

print(comp1.process(15))                            # calling method
print(comp2.process(20))

# To see how many instance variables an object is holding with there values
print(comp1.__dict__)
print(comp2.__dict__)