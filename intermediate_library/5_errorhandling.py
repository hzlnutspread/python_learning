# errors and exceptions
# syntax error vs exceptions

# syntax error
# a = 5 print(a)
# missing or too many parenthesis
# a = 5 + '10' will give type error
# ModuleNotFoundError if you import the wrong thing
# FileNotFoundError
# ValueError if you try to remove something from a list that doesn't exist
# IndexError if you try access an index from a list that doesn't exist

# #  you want to create your own error
# x = -3
# if x < 0:
#     raise Exception('x should be positive')
# else:
#     print(x)
#
# # using the asset keyword
# y = -5
# assert (y >= 0), 'x is not positive'

# try: except blocks
try:
    a = 5 / 0
except Exception as e:
    print(e)
else:
    print('all is fine')
finally:
    print("cleaning up")


# creating your own error
class ValueTooHighError(Exception):
    pass


class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high!')

    if x < 5:
        raise ValueTooSmallError('value is too small!', x)


try:
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)