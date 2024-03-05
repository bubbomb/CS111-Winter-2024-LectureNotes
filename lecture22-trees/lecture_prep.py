

def count_leaves(tree):

    if not tree.branches:
        return 1

    total = 0
    for branch in tree.branches:
        total += count_leaves(branch)
    
    return total

def double_tree(tree):
    tree.label = tree.label * 2
    for branch in tree.branches:
        double_tree(branch)
    return tree


def count_paths(tree, total):
    total_paths = 0
    if total == tree.label:
        total_paths += 1

    for branch in tree.branches:
        total_paths += count_paths(branch, total - tree.label)
    return total_paths