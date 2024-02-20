from tdd import square, add, factorial
import pytest

def test_square_1():
    assert square(1) == 1

def test_square_2():
    assert square(2) == 4

def test_square_3():
    assert square(3) == 9

def test_square_neg_1():
    assert square(-1) == 1

def test_square_half():
    assert square(0.5) == 0.25

def test_square_half():
    assert square(0.5) == 0.25


def test_add_1_2():
    assert add(1,2) == 3

def test_add_3_2():
    assert add(3,2) == 5

def test_add_3_10():
    assert add(3,10) == 13

def test_add_floats():
    assert add(0.625, 0.126) == 0.751

def test_add_3_nums():
    assert add(1,1,1) == 3

def test_add_4_nums():
    assert add(1,1,1,1) == 4

def test_add_5_nums():
    assert add(1,1,1,1,1) == 5

def test_add_6_nums():
    assert add(1,1,1,1,1,1) == 6

def test_add_1_num():
    with pytest.raises(TypeError):
        add(1)

def test_add_list():
    num_list = [1,2,3]
    num_list = [1,2,3]
    assert add(num_list, num_list) == num_list + num_list



def test_factorial_1():
    assert factorial(1) == 1

def test_factorial_2():
    assert factorial(2) == 2 * 1

def test_factorial_3():
    assert factorial(3) == 3 * 2 * 1

def test_factorial_4():
    assert factorial(4) == 4 * 3 * 2 * 1

def test_factorial_5():
    assert factorial(5) == 5 * 4 * 3 * 2 * 1