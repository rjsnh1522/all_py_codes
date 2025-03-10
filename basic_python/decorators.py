import time
from functools import wraps


def decorators(func):
    """function based decorators"""
    def wrapper(*args, **kwargs):
        print("Start")
        result = func()
        print("End")
        return result
    return wrapper



@decorators
def say_hello():
    print("Hello")



class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Before function call")
        result = self.func(*args, **kwargs)
        print("After function call")
        return result

@MyDecorator
def say_hello2(name):
    print(f"Hello {name=}")


def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f" calling {func.__name__} with args {args} kwargs {kwargs}")
        result  = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper


@log_decorator
def add(a, b):
    return a+b



# adding params to decorators

def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator



# functools wrap


# without func tools
def decorator_without_wraps(func):
    def wrapper(*args, **kwargs):
        print("before")
        result = func(*args, **kwargs)
        print("after")
        return result
    return wrapper


def decorator_with_wraps(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("before")
        result = func(*args, **kwargs)
        print("after")
        return result
    return wrapper

@decorator_without_wraps
def say_hello3():
    """ this is a doc string """
    print("Hello")


@decorator_with_wraps
def say_hello4():
    """ This is in 4th say hello """
    print("Hello")




## RETRY WITH DELAY using decorators

def retry(max_retires=3, delay=1):
    """" Some use full docstring"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retires:
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    retries += 1
                    if retries == max_retires:
                        print("Max retires reached")
                        raise e
                    print(f"Attempt {retries} failed: {e}. Retrying in {delay} second(s)...")
                    time.sleep(delay)
        return wrapper
    return decorator


@retry(max_retires=3, delay=1)
def unreliable_function():
    import random
    if random.random() < 0.7:
        raise ValueError("Error")
    return "Success"


if __name__ == "__main__":
    # say_hello()
    # say_hello2("Pawan")
    # add(2, 3)

    # print(say_hello3.__doc__)
    # print(say_hello3.__name__)
    #
    # print(say_hello4.__doc__)
    # print(say_hello4.__name__)

    res = unreliable_function()
    print(res)