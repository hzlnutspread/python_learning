# exception = events detected during an execution that interrupts normal flow of a program

numerator = int(input("Enter a number to divide: "))
denominator = int(input("Enter a number to divide by: "))

result = numerator / denominator
print(int(result))
# if we enter in a denominator of 0 then we get an error. ZeroDivisionError


# Basic form of exception handling is to put the code into a try: block
try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
    print(int(result))
except Exception: # not good practice to have one except block
    print("Something fucked up :'(")


# better way to do things is like this:
try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
    print(int(result))
except ZeroDivisionError as e: # good practice to catch specific exceptions
    print(e)
    print("You can't divide by 0! Stupid idiot!")
except ValueError as e:
    print(e)
    print("Enter only numbers please. Stupid monkey!")
except Exception as e:
    print(e)
    print("Something fucked up :'(")
else:
    print(result)
finally:
    print("Closing file")
