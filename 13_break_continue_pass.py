# Loop control statements change loops execution from its normal sequence

# break = terminate the loop entirely
# continue = skips to the next iteration of the loop
# pass = does nothing, acts as placeholder

while True:
    name = input("Enter your name: ")
    if name != "":
        break


# another way of writing this is
while True:
    name = input("Enter your name: ")
    if name:
        break


# we have phone number but we don't want to show the dashes
phone_number = "123-456-7890"
for i in phone_number:
    if i == "-":
        continue
    print(i, end="")


# i want to print number 1 to 20 but i don't like the number 13
for i in range(1, 21):
    if i == 13:
        pass
    else:
        print(i)

