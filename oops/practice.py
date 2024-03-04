#Hybrid Inheritance
class Grandfather:
    def old(self):
        print("Im old")
class Father(Grandfather):
    def teach(self):
        print("im teaching")
class Mohter:
    def cook(self):
        print("Im cooking")
class Child(Father,Mohter):
    def play(self):
        print("im playing")
obj=Child()
obj.old()
obj.teach()
obj.cook()
obj.play()









