class employee :
    age = 21
    salary = 1400000
    language = "python" # this is a class atribute


      # this is dunder method which is automaticaly call hota he jab bhi ham ek new object banate he tab
    def __init__(self,name ,salary,age,): 
        self.name = name 
        self.salary = salary
        self.age = age
        print("i am creating an object")

    def getInfo(self):
        print(f"the langauge is {self.language}. the salary is {self.salary}")
    
    def getbike(self):
        print("the my bike is ZX10r")

Aniket = employee("Aniket Gosavi",1400000,21) # this is object 
# Aniket.language = "javascript" # this is a instance atribute
print(Aniket.name , Aniket.salary,Aniket.age)

#karan = employee() # this is second object yaha call hoga auto init vala constructor 