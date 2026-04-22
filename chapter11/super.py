class GrandParent:
    def __init__(self):
        print("i am grandparent")
    
    def grandparentMethod(self):
        print("this is grandparent method")

class Parent(GrandParent):
    def __init__(self):
        super().__init__()  # Call the constructor of GrandParent
        print("i am parent")
    
    def parentMethod(self):
        print("this is parent method")


class Child(Parent):
    def __init__(self):
        super().__init__()  # Call the constructor of Parent
        print("i am child")
    
    def childMethod(self):
        print("this is child method")

c = Child()
c.grandparentMethod()  # this is grandparent method
c.parentMethod()       # this is parent method
c.childMethod()        # this is child method


