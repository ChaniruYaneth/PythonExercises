class Pet ():
    name = None
    fullness = 0
   
    def __init__(self, name):
        self.name = name
       
    def eat(self, food):
        print(self.name + " is eating " + food + "...")
        if food == "carrots":
            self.fullness = self.fullness + 10
        elif food == "grass":
            self.fullness = self.fullness + 5
        elif food == "water":
            self.fullness = self.fullness + 1
           
        print(self.name + " is now " + self.fullness + "...")
        
pet_owner_name = input("What is your name?")
print("Welcome, ", pet_onwner_name)


pet_1 = Pet("Rocky")


#carrots - 10 fullness
#grass - 5 fullness
#water - 1 fullness
