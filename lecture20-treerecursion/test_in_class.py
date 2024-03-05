from in_class import count_partition

def test_count_partition_1_0():
    assert count_partition(1,0) == 0

def test_count_partition_0_1():
    assert count_partition(0,1) == 1

def test_count_partition_3_2():
    assert count_partition(3,2) == 2

def test_count_partition_3_1():
    assert count_partition(3,1) == 1

def test_count_partition_4_2():
    assert count_partition(4,2) == 3

def test_count_partition_4_1():
    assert count_partition(3,1) == 1