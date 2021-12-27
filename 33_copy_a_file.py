import shutil
    # copyfile() = copies contents of a file
    # copy() = copyfile() + permission mode + destination can be directory
    # copy2() = copy() + copies metadata (file's creation and modification times


shutil.copyfile("C:\\Users\\ken\\Desktop\\test.txt", "C:\\Users\\ken\\Desktop\\copy.txt")
# within copyfile() function are two arguments; source and destination
# copy() and copy() do the same things