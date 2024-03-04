#two parents and one child realtion
class Father:
    def read(self):
        print("im reading")
    def code(self):
        print("im coding")
class Mother:
    def walk(self):
        print("im walking")
    def code(self):
        print("i can code")
class Boy(Father,Mother):
    def dance(self):
        print("im dancing")
    def code(self):
        print("i write code")

#Method Resolution Operator(MROif we have same method names in three classes then
# object of the reference first check in its own method if the method is there it
# can take that if ithas not that  method it will check in Father because in Boy
# class we can call Father first after that it will check in Mother class,....
# If in boy class if mother calls first then Mother's method will print

obj=Boy()
obj.read()
obj.walk()
obj.dance()
obj.code()
print(Boy.mro())















