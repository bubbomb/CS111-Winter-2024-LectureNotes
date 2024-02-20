def sum_digits(n):
    if n < 10:
        return n
    else:
        last = n % 10
        all_but_last = n // 10
        return last + sum_digits(all_but_last)
        
def luhn_sum(n):
    reversed_digits = reversed(str(n))
    total = 0
    for i, digit in enumerate(reversed_digits):
        digit = int(digit)
        if is_even(i):
            total += sum_digits(digit*2)
        else:
            total += digit

    return total

def is_even(n):
    return n % 2 != 0

