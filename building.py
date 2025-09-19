class Building:
    def __init__(self,name,type,power = 0):
        # Attributes
        # 1 : name
        self.name = name
        #2 : type ( Resdential , Commercial , hospital , school)
        self.type = type
        self.power = power
    
    def supply_power(self,new_power):
        self.power += new_power

    def consume_energy(self,new_power):
        self.power -= new_power

    def __str__(self):
        return "Building Info :\n Name : {}\n Type : {}\n Power : {}".format(self.name,self.type,self.power)

    def __eq__(self, value):
        return self.type == value.type
    


# b1 = Building("house","Resdential")
# print(b1)
# b1.supply_power(100)
# print(b1)
# b1.consume_energy(200)
# print(b1)

# b2 = Building("sift","school")
# print(b1 == b2)

