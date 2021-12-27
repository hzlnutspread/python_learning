# if statement is a block of code that executes only if it's condition is true

age = int(input("How old are you: "))

# Any indent signifies the block of code that runs for a particular if statement
if age > 18:
    print("You are an adult!")
elif age == 18:
    print("You are barely an adult...")
elif age < 0:
    print("That's not possible, try again you liar")
else:
    print("You are not an adult!")

