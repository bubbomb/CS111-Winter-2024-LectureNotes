from mergesort import merge_sort

def test_mergesort_base():
     assert merge_sort([1]) == [1]

def test_mergesort_1_2():
     assert merge_sort([1,2]) == [1,2]

def test_mergesort_2_1():
     assert merge_sort([2,1]) == [1,2]

def test_mergesort_2_1_3():
     assert merge_sort([2,1,3]) == [1,2,3]

def test_mergesort_bigger():
     assert merge_sort([2,1,3,-1, 5, 9]) == [-1,1,2,3,5,9]