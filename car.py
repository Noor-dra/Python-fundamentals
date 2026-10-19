class Car:
    def __init__ (self,type):
        self.type=type
    def start(self):
        print("car started.")
    def stop(self):
        print("car stopped")


class Toyota(Car):
    def __init__(self,brand,type):
        self.brand=brand
        super().__init__(type)
        super().start()
        super().stop()
 
class Fortuner(Toyota):
    def __init__(self,colour,brand,type):
        self.color=colour
        super().__init__(brand,type)

car1=Fortuner(colour="black",brand="new",type="electric")                       
print(f"Brand: {car1.brand}")
print(f"type:{car1.type}")
print(f"Color: {car1.color}")