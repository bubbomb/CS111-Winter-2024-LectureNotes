from animal import Elephant

def invert(x):
    inverse = 1/x # Raises a ZeroDivisionError if x is 0
    print('Never printed if x is 0')
    return inverse

def invert_safe(x):
    try:
        return invert(x)
    except ZeroDivisionError as e:
        print('Handled', e)
        return 0

try:
    invert_safe(0)
except ZeroDivisionError as e:
    print('Handled!')

ollie = Elephant('ollie')
print(ollie)
