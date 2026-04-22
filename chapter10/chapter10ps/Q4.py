import random


class trian :
    def __init__(self,trainNo,fro,to):
        self.trainNo = trainNo
        self.fro = fro
        self.to = to
        

    def book (self):
        print(f"the train number is {self.trainNo} and the train is going from {self.fro} to {self.to}")

    def getstatus(self):
        print(f"the train number is {self.trainNo} and the train is on time")

    def getfare(self):
        print(f"the train number is {self.trainNo} from {self.fro} to {self.to} is {random.randint(100,500)}")


train1 = trian(12345,"pune","mumbai")
train1.book()
train1.getstatus()
train1.getfare()
