from count_partitions import count_partitions

def test_count_partitions_fail():
    assert count_partitions(50, 6) == 3

def test_count_partitions_1_0():
    assert count_partitions(1,0) == 0

def test_count_partitions_0_2():
    assert count_partitions(0,2) == 1

def test_count_partitions_1_1():
    assert count_partitions(1,1) == 1

def test_count_partitions_2_1():
    assert count_partitions(2,1) == 1

def test_count_partitions_3_1():
    assert count_partitions(3,1) == 1

def test_count_partitions_3_2():
    assert count_partitions(3,2) == 2

def test_count_partitions_4_2():
    assert count_partitions(4,2) == 3

def test_count_partitions_6_4():
    assert count_partitions(6,4) == 9

def test_count_partitions_6_5():
    assert count_partitions(6,5) == 10

def test_count_partitions_10_2():
    assert count_partitions(10,2) == 6

def test_count_partitions_10_3():
    assert count_partitions(10,3) == 14

def test_count_partitions_2_4():
    assert count_partitions(2,4) == 2
