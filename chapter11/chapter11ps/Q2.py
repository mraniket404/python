class Animals:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class pet(Animals):
    def __init__(self,name,age,owner):
        super().__init__(name,age)
        self.owner = owner

class dog(pet):
    def __init__(self,name,age,owner,breed):
        super().__init__(name,age,owner)
        self.breed = breed
    def info(self):
        print(f"the name of dog is {self.name} and age is {self.age} and owner is {self.owner} and breed is {self.breed}")
d = dog("tommy",2,"Aniket","German shepherd")
d.info()
