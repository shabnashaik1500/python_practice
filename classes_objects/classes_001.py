#classes are blueprints to create objects
#objects are real world projects
#classes are having attributes and methods

#to create class
#attributes
class Person():
    name=None
    age=None
    gender=None
#methods
    def walk(self):
        print("im walking")
    def run(self):
        print("im running")
    def sleep(self):
        return ("im sleeping")
negan_object=Person()
shabna_object=Person()
negan_object.name="Negan"
negan_object.age=3
negan_object.gender="Male"
negan_object.walk()
negan_object.run()
shabna_object.name="shabna"
shabna_object.walk()













