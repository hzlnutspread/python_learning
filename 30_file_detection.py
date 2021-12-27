import os

path = "C:/Users/ken/Desktop/test.txt"
path2 = "C:\\Users\\ken\\Desktop\\folder"


if os.path.exists(path):
    print("This location exists")
    if os.path.isfile(path):
        print("That is a file")
else:
    print("This location doesn't exist")


if os.path.exists(path2):
    print("This location exists")
    if os.path.isfile(path2):
        print("That is a file")
    elif os.path.isdir(path2):
        print("That is a directory")
else:
    print("This location doesn't exist")