from recursion_practice import sum_nums, sum_up_to, reverse, funky_case

def test_sum_nums_base():
    assert sum_nums([1]) == 1

def test_sum_nums_1_2():
    assert sum_nums([1,2]) == 3

def test_sum_nums_3():
    assert sum_nums([3]) == 3

def test_sum_nums_1_2_3():
    assert sum_nums([1,2,3]) == 6

def test_sum_nums_big():
    assert sum_nums([1,2,3,1,1,1,1,5]) == 15

def test_sum_nums_empty():
    assert sum_nums([]) == 0



def test_sum_up_to_1():
    assert sum_up_to(1) == 1

def test_sum_up_to_2():
    assert sum_up_to(2) == 3

def test_sum_up_to_3():
    assert sum_up_to(3) == 6

def test_sum_up_to_5():
    assert sum_up_to(5) == 15



def test_reverse_a():
    assert reverse('a') == 'a'

def test_reverse_b():
    assert reverse('b') == 'b'

def test_reverse_me():
    assert reverse('me') == 'em'

def test_reverse_draw():
    assert reverse('draw') == 'ward'


def test_funky_case_a():
    assert funky_case('a') == 'a'

def test_funky_case_B():
    assert funky_case('B') == 'b'

def test_funky_case_Ba():
    assert funky_case('Ba') == 'bA'

def test_funky_case_lol():
    assert funky_case('lol') == 'lOl'

def test_funky_case_hello():
    assert funky_case('hello') == 'hElLo'
