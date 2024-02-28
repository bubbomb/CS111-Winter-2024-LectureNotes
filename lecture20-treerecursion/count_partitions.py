
def count_partitions(num, max_size_partition, counter=[0]):

    counter[0] = counter[0]+1
    print(counter)


    if max_size_partition <= 1:
        return max_size_partition

    if num == 0:
        return 1

    if num < 0:
        return 0


    left_leg = count_partitions(num-max_size_partition, max_size_partition)
    right_leg = count_partitions(num, max_size_partition-1)
    return right_leg + left_leg