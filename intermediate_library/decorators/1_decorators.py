# decorators

# the dosomething function is extended with the functionality of the decorator
# functions in python are first class objects. They can be defined inside another function, used as arguments or returned from other functions

# @mydecorator
# def dosomething():
#     pass
import functools


def start_end_decorator(func):
    @functools.wraps(
        func)  # so that python knows the identity of the functions. Preserves information of the used function
    def wrapper(*args, **kwargs):  # applying arguments
        print("start")
        result = func(*args, **kwargs)
        print("end")
        return result

    return wrapper


@start_end_decorator
def print_name():
    print("ken")


# print_name = start_end_decorator(print_name)
print_name()
print("-" * 20)


@start_end_decorator
def add5(x):
    result = x + 5
    print(result)


result = add5(10)
print("-" * 20)

print(add5.__name__)  # need to use the functools.wrap annotation to preserve the info
print("-" * 20)