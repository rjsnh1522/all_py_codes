

class DataStoreMixin:

    def big_method_in_mixin(self):
        print(self._b)
        print("big_method_in_mixin")

    def huge_method_in_mixin(self):
        print(self._c)
        print("huge_method_in_mixin")
