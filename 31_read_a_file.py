# how to read contents of a file
try:
    with open("C:\\Users\\ken\\Desktop\\test.txt") as file:  # using 'with open' closes file after reading them
        print(file.read())
except FileNotFoundError as e:
    print(e)
    print("Can not locate this file")
