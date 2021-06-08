import functools
import Lib
functions = []
register_function = functools.partial(
    Lib.register_function, functions
)

@register_function
def bigMethod(self):
    print("State is passed big Method")

@register_function
def hugeMethod(self):
    print("State is passed huge Method ")
