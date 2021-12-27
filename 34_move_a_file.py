import os

source = "test.txt"
destination = "C:\\Users\\ken\\Desktop\\test.txt"

source2 = "folder"
destination2 = "C:\\Users\\ken\\Desktop\\folder"

try:
    if os.path.exists(destination):
        print("There is already a file with the same name there")
    else:
        os.replace(source, destination)
        print(source + " was moved")
except FileNotFoundError as e:
    print(e)
    print(source + " was not found")


try:
    if os.path.exists(destination2):
        print("There is already a file with the same name there")
    else:
        os.replace(source2, destination2)
        print(source2 + " was moved")
except FileNotFoundError as e:
    print(e)
    print(source2 + " was not found")