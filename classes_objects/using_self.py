#self is a special variable which reference the instance of a class

class Car():
    name="Tesla"
    model="B12"
    color="red"
    def satrt(self):
        print("im starting",self.name)
    def engine(self):
        print("engine is strong")
tesla_object=Car()
tesla_object.satrt()
maruthi_obj=Car()
maruthi_obj.name="maruthi"
maruthi_obj.engine()
maruthi_obj.satrt()
