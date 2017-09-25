class Animal(object):
    hunger = 50
    thirst = 50

    def eat(self):
        self.hunger -= 1

    
    def drink(self):
        self.thirst -= 1

    
    def play(self):
        self.hunger += 1
        self.thirst += 1


racoon = Animal()
print(racoon.hunger, racoon.thirst)
racoon.eat()
racoon.drink()
print(racoon.hunger, racoon.thirst)
racoon.play()
print(racoon.hunger, racoon.thirst)
