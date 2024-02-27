# 1. Write production code only to pass a failing unit test.

# 2. Write no more of a unit test than sufficient to fail (compilation failures are failures).

# 3 .Write no more production code than necessary to pass the one failing unit test.

def square(n):
    return n * n

def add(*args):
    
    if isinstance(args[0], list):
        args = args[0]
    elif len(args) <= 1:
        raise TypeError('Needs at least 2 args')
    sum = 0
    for digit in args:
        sum += digit

    return sum
