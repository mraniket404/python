class employee :
    age = 21
    salary = 1400000
    language = "python" # this is a class atribute

    def getInfo(self):
        print(f"the langauge is {self.language}. the salary is {self.salary}")
    


Aniket = employee()
# Aniket.language = "javascript" # this is a instance atribute
Aniket.getInfo()