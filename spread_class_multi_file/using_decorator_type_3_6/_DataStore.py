import Lib
__method__ = []
register_method = Lib.register_method(__method__)

@register_method
def bigMethod(self):
    print("Printing B")
    return self._b

@register_method
def hugeMethod(self):
    print("Printing C")
    return self._c
