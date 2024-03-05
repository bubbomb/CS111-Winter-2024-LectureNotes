from in_class import sum_nums, sum_up_to, reverse, funky_case

def test_base_case():
    assert sum_nums([]) == 0

def test_4():
    assert sum_nums([4]) == 4

def test_7():
    assert sum_nums([7]) == 7

def test_7_4():
    assert sum_nums([7,4]) == 11

def test_7_4_2_1():
    assert sum_nums([7,4,2,1]) == 14

def test_slide():
    assert sum_nums([-32, 0, 32]) == 0



def test_sum_up_to_base():
    assert sum_up_to(1) == 1

def test_sum_up_to_2():
    assert sum_up_to(2) == 3

def test_sum_up_to_3():
    assert sum_up_to(3) == 6

def test_sum_up_to_5():
    assert sum_up_to(5) == 15


def test_reverse_base():
    assert reverse('b') == 'b'

def test_reverse_racecar():
    assert reverse('racecar') == 'racecar'

def test_reverse_ab():
    assert reverse('ab') == 'ba'

def test_reverse_abc():
    assert reverse('abc') == 'cba'


def test_funky_case_base():
    assert funky_case('t') == 't'

def test_funky_case_base_capital():
    assert funky_case('T') == 't'

def test_funky_case_tw():
    assert funky_case('tw') == 'tW'

def test_funky_case_wt():
    assert funky_case('Wt') == 'wT'

def test_funky_case_two():
    assert funky_case('two') == 'tWo'

def test_funky_case_hannah():
    assert funky_case('hannah') == 'hAnNaH'