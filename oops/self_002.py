class myClass():
    name=None
    age=Noneaddress=None
    def read(self):
        print("Im reading",self.name)
    def sleep(self):
        print("sleeping")
shabna_obj=myClass()
shabna_obj.name="shabna"
shabna_obj.age=33
negan_obj=myClass()
negan_obj.name="Negan"
negan_obj.age=3
shabna_obj.read()
negan_obj.read()