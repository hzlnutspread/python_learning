def get_square_numbers():
    num_list = [1, 4, 9, 25, 36, 49, 64, 81, 100]
    for i in num_list:
        print(i)


def iterable_square_numbers(cap):
    x = 0
    while x < cap:
        x = x + 1
        nums = x * x
        yield nums


if __name__ == "__main__":
    square_nums = iterable_square_numbers(5)
    for i in square_nums:
        print(i)