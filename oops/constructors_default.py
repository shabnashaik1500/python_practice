#constructor is a method for initializing the instance variables of a class
#constructors calles automatically when an object is created
#constructors uses by __init__ method
#constructors are two types
#Defaukt constructor(constructor with no arguments)
#parametarised constructor(constructor with arguments)

#default construcotr
class myClass():
    def __init__(self):
        self.x=20
        self.y=10
        print("addition is:",self.x+self.y)
obj=myClass()
#parametarized constructor
class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("attributes are:",self.name,self.age)
obj2=Person("shabna",33)


















