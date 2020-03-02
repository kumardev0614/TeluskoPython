# Here we will learn basics about init
# __init__ method is used as constructor for any object, like constructor __init__ also automatically gets
# called at object creation

class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def show_config(self):
        print("configuration is: Ram =", self.ram, 'and Cpu =', self.cpu)


comp1 = Computer('i5', 16)
comp2 = Computer('i7', 8)

comp1.show_config()
comp2.show_config()