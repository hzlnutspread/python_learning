# nested loops = loop inside of a loop.
# all inner loop interations will finish before the next interation of the outer loop starts

# rectangle drawn out of a symbol.

rows = int(input("How many rows? "))
columns = int(input("How many columns? "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()

# if we dont have end="" then each time we print the symbol our cursor will move down to the next line

