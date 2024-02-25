class myClass():
    name=None
    age=None
    def working(self):
        print("im working->",self.name)
shabna_object=myClass()
shabna_object.name="shabna"
shabna_object.age=33
negan_obj=myClass()
negan_obj.name="negan"
shabna_object.working()
negan_obj.working()