class GroundVehicle():

    def __init__(self, num_wheels=4):

        self.num_wheels = num_wheels

    def drive(self):
        print("vroooom")

x = GroundVehicle()
x.drive()


class Motorcycle(GroundVehicle):
    def __init__(self, num_wheels=2):
        super().__init__(num_wheels)
        self.num_wheels = num_wheels
    
    def __repr__(self):

        return f"<Motorcycle: {self.num_wheels}>"

    def drive(self):
        print("BRAAAP!!")    

q = Motorcycle()
q.drive()   

vehicles = [

    GroundVehicle().drive(),

    GroundVehicle().drive(),

    Motorcycle().drive(),

    GroundVehicle().drive(),

    Motorcycle().drive(),

]

vehicles

# testing wheels on Motorcycle
z = Motorcycle()
print(z)
