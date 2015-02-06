__author__ = 'Beni'

class Pet():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.indoor = False


    def getName(self):
        return self.name

polly = Pet("Polly", "Parrot")
kit = Pet("Kitty", "Cat")
print polly.name
print polly.species

kit.name = "The Ketten"

print kit.name