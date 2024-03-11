
def merge(list1, list2):
    new_list = []
    
    while len(list1) > 0 and len(list2) > 0:

        if list1[0] < list2[0]:
            new_list.append(list1.pop(0))
        else:
            new_list.append(list2.pop(0))
    
    new_list = new_list + list1 + list2

    return new_list

def merge_sort(unsorted_list):
    if len(unsorted_list) == 1:
        return unsorted_list

    midpoint = len(unsorted_list) // 2
    sorted_first_half = merge_sort(unsorted_list[:midpoint])
    sorted_second_half = merge_sort(unsorted_list[midpoint:])

    return merge(sorted_first_half, sorted_second_half)