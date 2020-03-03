# 3) So here are two classes with execute() method in it.

class pyCharm:
    def execute(self):
        print('compiling')
        print('executing')


class myEditor:
    def execute(self):
        print('spelcheck')
        print('compiling')
        print('executing')


class laptop:

    def code(self, ide):    # 1 )Here we a method which takes some argument
        ide.execute()       # 2)But that argument is used to call a method, and a variable thing which can call a method
        # 2.0) is object. So here we have to pass an object of that class who has execute() method in it.


instanceOfPycharm = pyCharm()

instanceOfMyEditor = myEditor()


# 4) But which method will run depends on object passed in code(self, ide) method.
lap1 = laptop()
lap1.code(instanceOfPycharm)
print()
lap1.code(instanceOfMyEditor)


