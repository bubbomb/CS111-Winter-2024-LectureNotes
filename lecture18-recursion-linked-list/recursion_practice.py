

def sum_nums(nums):
    if nums == []:
        return 0
    return nums[0] + sum_nums(nums[1:])

def sum_up_to(num):
    # total = 0
    # for i in range(1, num+1):
    #     total += i

    # return total

    if num == 1:
        return num
    return num + sum_up_to(num-1)


def reverse(word):
    if len(word) == 1:
        return word

    return word[-1] + reverse(word[:-1])


def funky_case(word, up_case=False):
    if len(word) == 1:
        return toggle_case(word, up_case)

    first_letter = word[0]
    return toggle_case(first_letter, up_case) + funky_case(word[1:], not up_case)

def toggle_case(letter, should_up_case):
    return letter.upper() if should_up_case else letter.lower()