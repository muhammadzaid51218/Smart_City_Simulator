from building import Building

class Citizen:
    def __init__(self,name,age,job,home):
        self.name = name
        self.age = age
        self.job = job
        self.home = home
    
    def go_to_work(self):
        print("{} is going to work as a {}.".format(self.name,self.job))

    def pay_bill(self):
        print("{} is paying a bill.".format(self.name))

    def use_transport(self):
        print("{} is using transportation".format(self.name))

    def __len__(self):
        return self.age
    
    def __call__(self,action):
        if action == "work":
            self.go_to_work()
        elif action == "pay":
            self.pay_bill()
        elif action == "transport":
            self.use_transport()
        else:
            print("Unknown action : {}.".format(action))




# c1 = Citizen("zaid",18,"no","yes")
# print(len(c1))
# c1.go_to_work()
# c1.pay_bill()
# c1.use_transport()
# c1("work")
# c1("pay")
# c1("transport")
# c1("other")


b1 = Building("house","Resdential")
print(b1)