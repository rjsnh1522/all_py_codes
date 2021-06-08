def add_functions_to_class(functions):
    def decorator(ClassName):
        for function in functions:
            setattr(ClassName, function.__name__, function)
        return ClassName
    return decorator


def register_function(sequence, function):
    sequence.append(function)
    return function
