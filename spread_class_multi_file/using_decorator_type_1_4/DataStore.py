import Lib
import _DataStore


@Lib.add_functions_to_class((_DataStore.bigMethod, _DataStore.hugeMethod))

class DataStore:

    def some_other_method1(self):
        print("some_other_method1")

    def some_other_new_methods(self):
        print("some_other_new_methods")


d = DataStore()
d.bigMethod()
d.hugeMethod()
