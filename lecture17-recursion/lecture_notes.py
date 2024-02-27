def sum_digits(n):
    """Return the sum of the digits of positive integer n.
    >>> sum_digits(6)
    6
    >>> sum_digits(2023)
    7
    """
    if n < 10:
        return n
    else:
        all_but_last = n // 10
        last = n % 10
        return sum_digits(all_but_last) + last


print(sum_digits(6))
print(sum_digits(2023))


def luhn_sum(n):
    if n < 10:
        return n
    else:
        last = n % 10
        all_but_last = n // 10
        return last + luhn_sum_double(all_but_last)
        
def luhn_sum_double(n):
    last = n % 10
    all_but_last = n // 10
    luhn_digit = sum_digits(last * 2)
    if n < 10:
        return luhn_digit
    else:
        return luhn_digit + luhn_sum(all_but_last)


print(luhn_sum(62))
print(luhn_sum(5105105105105100))