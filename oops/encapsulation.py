# attributes and methods together in a class is encapsulation
# access specifiers
# public:we can use anywhere
# protected:we can use inside of the class and with in the drived class of the base class
# private:we can use only inside of the class

# public
class Person():
    def __init__(self, name):
        self.name = name
    def display(self):
        print(f"my name is:{self.name}")


obj = Person("shabna")
obj.display()

#protected
class Person2():
    def __init__(self, name, age):
        self.name = name
        self._age = age
    def _display_details(self,id,phn):
        self._id=id

class Person3(Person2):
    pass

obj2 = Person3("shabna", 33)
obj2._display_details(12,12345)#protected calling outside of the class

#private
class myDetails():
    def __init__(self,name,age,mobilenumber):
        self.name=name
        self._age=age
        self.__mobilenumber=mobilenumber
    def __display(self):
        print(f"my name is {self.name} and age is {self._age} and mobilenumber is{self.__mobilenumber}")
obj=myDetails("shabna",33,7382656498)
obj.__display()

































