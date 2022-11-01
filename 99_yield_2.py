def number_generator():
    x = 1
    yield x
    yield x + 1
    yield x + 2


generator_object = number_generator()
print(generator_object)

for i in generator_object:
    print(i)