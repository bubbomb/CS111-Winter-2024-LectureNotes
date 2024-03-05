def sum_nums(nums):
    """Returns the sum of the numbers in nums.
    >>> sum_nums([6, 24, 1984])
    2014
    >>> sum_nums([-32, 0, 32])
    0
    """

    if len(nums) == 0:
        return 0

    return nums[0] + sum_nums(nums[1:])


    # total = 0
    # for num in nums:
    #     total += num

    # return total


def sum_up_to(n):
    """Returns the sum of positive numbers from 1 
    up to n (inclusive).
    >>> sum_up_to(5)
    15
    """

    if n == 1:
        return 1
    return n + sum_up_to(n-1)


def reverse(word):
    """Returns a string with the letters of s
    in the inverse order.
    >>> reverse('ward')
    'draw'
    """

    if len(word) == 1:
        return word
    return reverse(word[1:]) + word[0]

def toggle_case(text, should_upper_case):
    if should_upper_case:
        return text.upper()
    return text.lower()

def funky_case(text, should_upper_case=False):
    """Returns text in fUnKyCaSe
    >>> fUnKyCaSe("wats up")
    'wAtS Up'
    """

    if len(text) == 1:
        return toggle_case(text, should_upper_case)

    first_letter = toggle_case(text[0], should_upper_case)
    next_letters = funky_case(text[1:], not should_upper_case)

    return first_letter + next_letters