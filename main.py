class Animal():

    def make_sound(self):
        pass

    def eat(self):
        pass

class Bird(Animal):
    def make_sound(self):
        print("кар-кар")

class Mammal(Animal):
    def make_sound(self):
        print("мяу")

class Reptile(Animal):
    def make_sound(self):
        print("щелкает челюстью")

animals = [Bird(), Mammal(), Reptile()]
def animal_sound(animals):
    animal.make_sound()

for animal in animals:
    animal_sound(animal)


