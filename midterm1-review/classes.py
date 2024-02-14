class Animal():
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
        return f"Animal named {self.name}. Age: {self.age}"

    def __repr__(self):
        return f"Animal({self.name}, {self.age})"

    def __add__(self, other):
        if isinstance(other, Animal):
            return [self, other]
        elif isinstance(other, int):
            self.age += other

cat = Animal('Garfield')
dog = Animal('Odie')

print(cat,dog)
print(cat + dog)
print(cat + 10)
print(cat)
