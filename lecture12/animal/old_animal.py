from random import choice, random, randint, randrange

class Food:

    def __init__(self, name, type, calories):
        self.name = name
        self.type = type
        self.calories = calories

class Organism:
    def play(self):
        pass
    def eat(self, food):
        pass

class Animal(Organism):
    species_name = "Animal"
    scientific_name = "Animalia"
    play_multiplier = 2
    interact_increment = 1
    calories_needed = 0

    def __init__(self, name, age=0):
        self.name = name
        self.age = age
        self.calories_eaten  = 0
        self.happiness = 0

    def __str__(self):
        return "Animal named " + self.name

    def play(self, num_hours):
        self.happiness += (num_hours * self.play_multiplier)
        print("WHEEE PLAY TIME!")

    def eat(self, food):
        self.calories_eaten += food.calories
        print(f"Om nom nom yummy {food.name}")
        if self.calories_eaten > self.calories_needed:
            self.happiness -= 1
            print("Ugh so full")

    def interact_with(self, animal2):
        self.happiness += 1
        print(f"Yay happy fun time with {self.name} and {animal2.name}")

    def happiness_check(self):
        print(f'{self.name}: happiness --> {self.happiness}')
    
    def mate_with(self, other):
        if other is not self and other.species_name == self.species_name:
            self.mate = other
            other.mate = self


class Rabbit(Animal):
    species_name = "European rabbit"
    scientific_name = "Oryctolagus cuniculus"
    calories_needed = 200

    num_in_litter = 12
    def reproduce_like_rabbits(self):
        if self.mate is None:
            print("oh no! better go on ZoOkCupid")
            return
        self.babies = []
        for _ in range(0, self.num_in_litter):
            self.babies.append(Rabbit("bunny", 0))

class Dog(Animal):
    species_name = 'Chihuahua'
    scientific_name = "Caninus Noisus"
    calories_needed = 500

    def play(self, num_hours):
        super().play(num_hours)
        print(f"{self.name} peed on the floor")
        print(f"{self.name} shivered uncontrollably")


def partytime(animals):
    """Assuming ANIMALS is a list of Animals, cause each
    to interact with all the others exactly once."""
    for i in range(len(animals)):
        for j in range(i + 1, len(animals)):
            animals[i].interact_with(animals[j])
