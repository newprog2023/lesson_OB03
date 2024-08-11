class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

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

#animals = [Bird(), Mammal(), Reptile()]
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

# animal_sound(animals)

class Zoo():
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f'Животное {animal.name} добавлено в зоопарк')

    def add_staff(self, new_staff):
        self. staff.append(new_staff)
        print(f'{new_staff} принят на работу в зоопарк')

class ZooKeeper(Zoo):
    def feed_animal(self, animal):
        print(f'Сотрудник кормит {animal.name}')

class Veterinarian(Zoo):
    def heal_animal(self, animal):
        print(f'Ветеринар лечит {animal.name}')


bird1 = Bird('Bорона', 1)
mammal1 = Mammal('Рысь', 2)
reptile1 = Reptile('Ящер', 3)
zoo = Zoo()
keeper = ZooKeeper()
vet = Veterinarian()

zoo.add_animal(bird1)
zoo.add_animal(mammal1)
zoo.add_animal(reptile1)

zoo.add_staff(keeper)
zoo.add_staff(vet)

animal_sound(zoo.animals)

keeper.feed_animal(mammal1)
vet.heal_animal(reptile1)