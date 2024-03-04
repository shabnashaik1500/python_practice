#constructors with arguments is caleed parametarized constructor
class myClass():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        print("addition is:",self.x+self.y)

obj=myClass(20,10)