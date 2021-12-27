# a return statement is used within functions to send python values/objects back to the caller
# these values/objects are known as the function's return values

def multiply(number1, number2):
    result = number1 * number2
    return result


# we can print the answer like this:
print(multiply(6, 8))

# or we can store the returned value within a variable
x = multiply(6, 8)
print(x)


# Another way to do this is as follows:
def multiply(number1, number2):
    return number1 * number2


x = multiply(6, 8)
print(x)
