def cube(k):
    return k ** 3

def square(k):
    return k**2

def add_one(k):
    return k+1

def summation(n, term):
    """Sum the first N terms of a sequence. TERM is a function
       that takes a single argument and returns a result.
    >>> summation(5, cube)
    225
    """
    total = 0
    k = 1
    while k <= n:
        total = total + term(k)
        k = k + 1
    return total


total = summation(5, cube)
print(total)
total = summation(5, square)
print(total)

total = summation(5, add_one)
print(total)

def make_adder(n):
    """Return a function that takes one argument k
       and returns k + n.
    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def adder(k):
        return k + n
    return adder
    
    
add_one = make_adder(1)
print(add_one(2))

print(make_adder(4)(5))