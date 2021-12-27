# slicing is used to create a substring by extracting elements from another string
# can you indexing[] or slice()
# [start:stop:step]

name = "Sniper Monkey"

# start is inclusive and stop is not inclusive
first_name = name[0:6]
print(first_name)

last_name = name[7:]
print(last_name)


# two colons means python takes first and last letters i.e entire string
funky_name = name[::2]
print(funky_name)


# to reverse a string
reversed_name = name[::-1]
print(reversed_name)


# if we want to take a portion of a string we can use the slice() function
# the -4 means we count from the end of the string with the first letter being at point -1
website = "http://google.com"
website2 = "http://yourmotherislarge.com"
slice = slice(7, -4)
print(website[slice])
print(website2[slice])

