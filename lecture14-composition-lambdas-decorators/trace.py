def trace1(f):
    """Return a function that takes a single argument, x, prints it,
    computes and prints F(x), and returns the computed value.
    >>> square = lambda x: x * x
    >>> trace1(square)(3)
    -> 3
    <- 9
    9
    """
    def traced(x):
        print("->", x)
        r = f(x)
        print("<-", r)
        return r
    return traced

@trace1
def square(x):
    return x * x

# def square(x):
#     return x * x
# square_with_trace = trace1(square)

print(square(8))
# print(square_with_trace(8))