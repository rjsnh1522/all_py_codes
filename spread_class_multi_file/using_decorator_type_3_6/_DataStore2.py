import Lib
__method__ = []
register_method = Lib.register_method(__method__)

@register_method
def big_method_in_data_store2(self):
    print("big_method_in_data_store2 B")
    return self._b

@register_method
def huge_method_in_data_store2(self):
    print("huge_method_in_data_store2 ")
    return self._c
