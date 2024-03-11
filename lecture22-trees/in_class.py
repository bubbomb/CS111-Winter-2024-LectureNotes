

def double_labels(my_tree):
    my_tree.label *= 2

    for branch in my_tree.branches:
        double_labels(branch)

def count_leaves(my_tree):
    
    if not my_tree.branches:
        return 1

    total = 0
    for branch in my_tree.branches:
        total += count_leaves(branch)
    return total