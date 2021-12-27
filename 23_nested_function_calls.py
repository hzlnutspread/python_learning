# nested functions calls are functions calls inside other function calls
# the innermost function calls are resolved first
# the returned value is used as an argument for the next outer function

num = input("Enter a whole positive number: ")
num = float(num)
num = abs(num)
num = round(num)
print(num)


# can do this with less code using nested function calls
print(round(abs(float(input("Enter a whole positive number: ")))))
