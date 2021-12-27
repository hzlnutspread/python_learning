# This creates a new file or overwrites an existing file

text = "Yooooo!\nThis is some text.\nHave a good one!"
text2 = "\nHave a nice day.\nSEEYA!"

with open("C:\\Users\\ken\\Desktop\\test.txt", 'w') as file:
    file.write(text)

with open("C:\\Users\\ken\\Desktop\\test.txt", 'a') as file:
    file.write(text2)

with open("C:\\Users\\ken\\Desktop\\test.txt") as file:
    print(file.read())

