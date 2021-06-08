# Polymorphism means the ability to take various forms.


class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("The animal noise")


class Cat(Animal):
    def __init__(self, name, fur_type):
        Animal.__init__(self, name)
        # or
        super().__init__(name)
        self.fur_type = fur_type

    def talk(self):
        print("Meow")


class Dog(Animal):
    def talk(self):
        print("Woof!")


animals = [Cat('Missy', 'short'),
           Cat('tom', 'short'),
           Cat('Thom', 'long'),
           Dog('Lassie')]

for ani in animals:
    print(ani.name)
    print(ani.talk())
