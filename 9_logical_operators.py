# logical operators (and, or, (not)) are used to check if two or more conditional statements are true

temp = int(input("What is the temperature outside?: "))

if temp >= 0 and temp <= 30:
    print("The temperature is good today")
    print("Go outside you nerd")

# simplified way of typing this is:
if 0 <= temp <= 30:
    print("The temperature is good today")
    print("Go outside you nerd")
elif temp < 0 or temp > 30:
    print("The temperature is bad today")
    print("Stay inside and code")

# not operator will take a conditional statement and if its true it will flip to false. If its normally false it will flip to to true.
if not (0 <= temp <= 30):
    print("The temperature is bad today")
    print("Stay inside and code")
elif not (temp < 0 or temp > 30):
    print("The temperature is good today")
    print("Go outside you nerd")
