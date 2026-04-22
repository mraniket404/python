class GrandParent:
    def __init__(self):
        print("i am grandparent")
    
    def grandparentMethod(self):
        print("this is grandparent method")

class Parent(GrandParent):
    def __init__(self):
        GrandParent.__init__(self)  # Direct call - no super()
        print("i am parent")
    
    def parentMethod(self):
        print("this is parent method")

class Child(Parent):
    def __init__(self):
        Parent.__init__(self)  # Direct call - no super()
        print("i am child")
    
    def childMethod(self):
        print("this is child method")

c = Child()
c.grandparentMethod()
c.parentMethod()
c.childMethod()