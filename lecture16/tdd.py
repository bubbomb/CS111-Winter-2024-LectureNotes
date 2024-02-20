# 1. Write production code only to pass a failing unit test.

# 2. Write no more of a unit test than sufficient to fail (compilation failures are failures).

# 3 .Write no more production code than necessary to pass the one failing unit test.

def square(x):
    return x ** 2

def add(*args):
    if len(args) == 1:
        raise TypeError("add() takes 2 or more arguments")

    if isinstance(args[0], list):
        sum = []
    else:
        sum = 0

    for arg in args:
        sum += arg
    return sum

def factorial(x):
    if x == 1:
        return 1
    total = 1
    prev_number = 1

    for _ in range(x):
        total *= prev_number
        prev_number += 1
    return total


    # if x == 0:
    #     return 1
    # return x * factorial(x-1)