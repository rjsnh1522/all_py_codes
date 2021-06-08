# decorators are function that takes other function as argument and add
# some kind of functionality without alerting the source code of original function you passed in
# example can be adding a logging feature or timing feature of any function

# Decorators
from functools import wraps


def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper

import time


@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('Tom', 22)












#
# class OuterFunction:
#     def __init__(self, original_func):
#         self.original_func = original_func
#
#     def __call__(self, *args, **kwargs):
#         print("in call", args[0])
#         return self.original_func(*args, **kwargs)
#
#
# @OuterFunction
# def display_two(name):
#     print("hi", name)
#
#
# display_two("Ramadhir")
#
# def outer_function(original_func):
#     def inner_function():
#         print("I am here")
#         return original_func
#     return inner_function()
#
# @outer_function
# def display():
#     print("Displaying")
#
# display()
#
#
