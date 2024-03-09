class Pet():
    name = None
    fullness = 0

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(self.name + " is eating " + food + "...")
        if food == "carrots":
            self.fullness += 10
        elif food == "grass":
            self.fullness += 5
        elif food == "water":
            self.fullness += 1

        print(self.name + " is now " + str(self.fullness) + " full.")  # Corrected print statement


pet_owner_name = input("What is your name? ")
print("Welcome,", pet_owner_name)

pet_1 = Pet("Rocky")

food_eaten = input("What should " + pet_1.name + " eat? ")  # Ask for the food eaten by the pet
pet_1.eat(food_eaten)  # Call the eat method with the food eaten by the pet
