from abc import ABC, abstractmethod


class Abstr(ABC):
    @abstractmethod
    def add(self):
        pass


class Demo(Abstr):
    def sub(self):
        print('gfdvdf')


class NewDemo(Demo):
    def add(self):
        print('added')


if __name__ == '__main__':
    print(NewDemo())
