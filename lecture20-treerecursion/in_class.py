

def count_partition(num, max_partition_size):

    if max_partition_size == 1:
        return 1
    if max_partition_size == 0:
        return 0
    if num < 0:
        return 0

    return count_partition(num-max_partition_size, max_partition_size) + count_partition(num, max_partition_size-1)

