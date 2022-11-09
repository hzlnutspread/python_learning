import functools

# Class decorators keep track of state
class CountCalls:

    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):  # allows class instances to behave like func and be called like a func
        self.num_calls += 1
        print(f'this is executed {self.num_calls} times')
        return self.func(*args, **kwargs)


@CountCalls
def say_hello():
    print("hello")


say_hello()
say_hello()