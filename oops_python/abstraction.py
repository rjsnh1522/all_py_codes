# on or more implementation

# can be considered as an abstract class
from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def talk(self):
        pass


class Cat(Animal):
    def __init__(self, name, fur_type):
        super().__init__(name)
        self.fur_type = fur_type

    def talk(self):
        print("Meow")


class Dog(Animal):
    def talk(self):
        print("woof")


d = Dog('Lassie')

d.talk()

# a = Animal('an')  # it will give error
# a.talk()
