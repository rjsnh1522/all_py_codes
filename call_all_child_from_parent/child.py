class Parent(object):
    def __init__(self):
        pass


class Foo(Parent):
    @staticmethod
    def run():
        print("run of Foo")

    @staticmethod
    def run2():
        print("run 2 of Foo")


class Bar(Parent):
    @staticmethod
    def run():
        print("run of bar")

    @staticmethod
    def run2():
        print("run 2 of Bar")
        return True


class Baz(Parent):
    @staticmethod
    def run():
        print("run of Baz")

    @staticmethod
    def run2():
        print("run 2 of Baz")


class Bing(Bar):
    @staticmethod
    def run():
        print("run of Bing")

    @staticmethod
    def run2():
        print("run 2 of Bing")


if __name__ == "__main__":
    print([cls.run2() for cls in Parent.__subclasses__()])
