class twoDvector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def show(self):
        print(f"the value of x is {self.x} and the value of y is {self.y}")    
    
class threeDvector(twoDvector):
    def __init__(self,x,y,z):
        super().__init__(x,y) # this is the way to call the constructor of parent class 
        self.z = z
    def show(self):
        print(f"the value of x is {self.x} and the value of y is {self.y} and the value of z is {self.z}")

a = twoDvector(1,2)
a.show()
b = threeDvector(1,2,3)
b.show()
