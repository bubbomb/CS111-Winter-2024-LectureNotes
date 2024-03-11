from tree import Tree

from in_class import double_labels, count_leaves

def test_double_base():
    test_tree = Tree(0)
    double_labels(test_tree)

    assert test_tree.label == 0

def test_double_1():
    test_tree = Tree(1)
    double_labels(test_tree)

    assert test_tree.label == 2

def test_double_1_branch():
    test_tree = Tree(1, [Tree(2)])
    double_labels(test_tree)

    assert test_tree.label == 2
    assert test_tree.branches[0].label == 4

def test_double_2_branches():
    test_tree = Tree(1, [
            Tree(2), 
            Tree(3), 
            ]
        )

    double_labels(test_tree)

    assert test_tree == Tree(2, [
        Tree(4),
        Tree(6),
    ])

def test_double_2_branches_deep():
    test_tree = Tree(1, [
            Tree(2, [
                Tree(4),
                Tree(5)
            ]), 
            Tree(3), 
            ]
        )

    double_labels(test_tree)

    assert test_tree == Tree(2, [
        Tree(4, [
            Tree(8),
            Tree(10)
        ]),
        Tree(6),
    ])


def test_count_leaves():
    test_tree = Tree(0)
    assert count_leaves(test_tree) == 1

def test_count_leaves():
    test_tree = Tree(1, [Tree(2)])
    assert count_leaves(test_tree) == 1

def test_count_leaves():
    test_tree = Tree(1, [
            Tree(2), 
            Tree(3), 
            ]
        )
    assert count_leaves(test_tree) == 2