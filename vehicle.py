class Vehicle:
    def __init__(self,type,fuel = 0,speed = 0):
        self.type = type
        self.fuel = fuel
        self.speed = speed

    def move():
        pass

    def refuel():
        pass

    def __add__(self,value):
        return Vehicle(self.type + value.type)
    

    def __sub__(self,value):
        return self.type - value.type

v1 = Vehicle(1)
v2 = Vehicle(2)

# print(v1 + v2)


