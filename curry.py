from inspect import signature


def curry(function):
    arguments = list()
    number_of_args = len(signature(function).parameters)

    def wrapper(*args):
        arguments.extend(args)
        if len(arguments) == number_of_args:
            return function(*arguments)
        else:
            return wrapper

    return wrapper


def sum(a, b):
    return a + b


csum = curry(sum)
print(csum()(1)()(1))
