import os
import shutil  # used to remove trees

file = "test.txt"
directory = "folder"

try:
    os.remove(file)  # function to delete a file
except FileNotFoundError as e:
    print(e)
    print("This file does not exist")
except PermissionError as e:
    print(e)
    print("You do not have the required permissions to delete this file")
else:
    print(file + " has been deleted")


try:
    os.rmdir(directory)  # function to delete a directory (can not delete if there are files inside directory)
except FileNotFoundError as e:
    print(e)
    print("This directory does not exist")
except PermissionError as e:
    print(e)
    print("You do not have the required permissions to delete this directory")
except OSError as e:
    print(e)
    print("You can not delete that using that function")
else:
    print(directory + " has been deleted")


try:
    shutil.rmtree()
except FileNotFoundError as e:
    print(e)
    print("This directory does not exist")
except PermissionError as e:
    print(e)
    print("You do not have the required permissions to delete this directory")
except OSError as e:
    print(e)
    print("You can not delete that using that function")
else:
    print(directory + " has been deleted")