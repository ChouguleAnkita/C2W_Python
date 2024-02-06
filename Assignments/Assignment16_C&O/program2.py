class Vehical:
    def __init__(self,brand,model,year,speed):
        self.brand=brand
        self.model=model
        self.year=year
        self.speed=speed
    
    def accelerate(self):
        print("In Accelerate")
    
    def brake(self):
        print("In brake")
    
    def honk(self):
        print("In honk")
class Child(Vehical):
    def __init__(self, brand, model, year, speed):
        pass

    def accelerate(self):
        print("In child class accelerate")
    
    def honk(self):
        print("In child class:honk")

brand=input("Enter brand:")
model=input("Enter model:")
year=int(input("Enter year"))
speed=input("Enter speed")
    
vObj=Vehical(brand,model,year,speed)
obj=Child(brand,model,year,speed)