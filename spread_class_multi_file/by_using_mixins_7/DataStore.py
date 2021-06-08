import _DataStore
import _DataLoad
import inspect


class DataStore(_DataStore.DataStoreMixin, _DataLoad.DataLoadMixin):
    def __init__(self):
        self._a = 1
        self._b = 2
        self._c = 3
        self.print_all_method()

    def small_method(self):
        print(self._a)

    def print_all_method(self):
        methods = inspect.getmembers(self, predicate=inspect.ismethod)
        for meth in methods:
            if meth[0] != "__init__" and meth[0] != "print_all_method":
                getattr(self, meth[0])()


d = DataStore()
