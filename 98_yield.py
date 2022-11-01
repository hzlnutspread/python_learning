class Iterable:
    # you are creating an iterable every time you instantiate the class so each time you create it it can be called
    def __iter__(self):
        x = 1
        yield x
        yield x + 1
        yield x + 2


iterable = Iterable()

for i in iterable:  # iterator is created here
    print(i)

for i in iterable:  # iterator is created again
    print(i)