from in_class_tdd import square, add
import pytest

def test_square_1():
    assert square(1) == 1

def test_square_2():
    assert square(2) == 4

def test_square_3():
    assert square(3) == 9

def test_square_10():
    assert square(10) == 100


def test_add_1_1():
    assert add(1,1) == 2

def test_add_2_1():
    assert add(2,1) == 3

def test_add_2_2():
    assert add(2,2) == 4

def test_add_2_2():
    assert add(2,2) == 4

def test_add_floats():
    assert add(0.1, 0.1) == pytest.approx(0.2)

def test_add_floats_point_3():
    assert add(0.1, 0.2) == pytest.approx(0.3)

def test_add_three_nums():
    assert add(1,1,1) == 3

def test_add_eight_nums():
    assert add(1,1,1,1,1,1,1,1) == 8

def test_add_throw_value_error():
     with pytest.raises(TypeError):
        add(1)

def test_add_list_of_numbers():
    assert add([1,2,3]) == 6
    