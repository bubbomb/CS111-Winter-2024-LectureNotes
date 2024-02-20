from luhn_sum import luhn_sum

def test_luhn_sum_2():
    assert luhn_sum(2) == 2

def test_luhn_sum_32():
    assert luhn_sum(32) == 8

def test_luhn_sum_62():
    assert luhn_sum(62) == 5

def test_luhn_sum_62():
    assert luhn_sum(62) == 5

def test_luhn_sum_large():
    assert luhn_sum(5105105105105100) == 20