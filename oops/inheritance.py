#to get the behaviour from parent class to newly created child class we can use inheritance
#to reduce time and lines of code
#single inheritance:one parent and one child relation
class Human:
    def __init__(self,num_eyes,num_nose):
        self.num_eyes=num_eyes
        self.num_nose=num_nose
    def read(self):
        print("im reading")
    def write(self):
        print("im writing")
class male(Human):
    def __init__(self,eyes,nose,num_heart):
        super().__init__(eyes,nose)
        self.num_heart=num_heart
    def walk(self):
        print("im walking")
#method overriding:if parent class and child class have same method name 
    # then method overriding will be happened ,and in that case child method will execute
    #but if we want to exexute both the parent and child methods then we  can use super()
    def read(self):
        super().read()
        print("i can read")
obj=male(2,1,1)
obj.write()
obj.read()
print(obj.num_eyes)
print(obj.num_nose)
print(obj.num_heart)




















