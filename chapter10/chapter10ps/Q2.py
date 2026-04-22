class calculator:

    def __init__(self , n):
        self.n = n

    def square(self):
        print(f"the value of {self.n} square is {self.n ** 2}") 

    def cube(self):
        print(f"the value of {self.n} cube is {self.n ** 3}")

    def squareroot(self):
        print(f"the value of {self.n} squareroot is {self.n ** 0.5}")

a = calculator(4)
a.square()
a.cube()
a.squareroot()
                