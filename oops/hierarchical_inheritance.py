#from one parent to multiple children
class Father:
    def read(self):
        print("im reading")
class Child1(Father):
    def walk(self):
        print("im walking")
class Child2(Father):
    def cook(self):
        print("im cooking")
obj=Child1()
obj.read()
obj2=Child2()
obj2.read()