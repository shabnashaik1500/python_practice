#combination of two or more inheritances is hybrid inheritance
class Grandfather:
    def read(self):
        print("im reading")
class Father(Grandfather):
    def walk(self):
        print("im walking")
class Mother:
    def cook(self):
        print("im cooking")
class Child(Father,Mother):
    def play(self):
        print("im playing")
obj=Child()
obj.read()
obj.walk()
obj.cook()
obj.play()









