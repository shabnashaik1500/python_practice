#from grandparent to parent to child realtion
class GrandFather:
    def read(self):
        print("im reading")
class Father(GrandFather):
    def write(self):
        print("im writing")
class Child(Father):
    def cook(self):
        print("im cooking")
obj=Child()
obj.read()
obj.write()
obj.cook()