def fibonacci(limit):
    # 0, 1 first numbers, 1, 2, 3, 5 etc...
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


fib = fibonacci(200)
for i in fib:
    print(i)
