from tree import Tree

from lecture_prep import count_leaves, double_tree, count_paths

def test_count_leaves_1():
    test_tree = Tree('first')

    assert count_leaves(test_tree) == 1

def test_count_leaves_1_node_1_leaf():
    test_tree = Tree(1, [Tree(2)])

    assert count_leaves(test_tree) == 1

def test_count_leaves_2_leaves():
    test_tree = Tree('not-leaf', [Tree('not-leaf', [Tree('leaf1'), Tree('leaf2')])])

    assert count_leaves(test_tree) == 2

def test_count_leaves_3_leaves():
    test_tree = Tree('node1', [Tree('node2', [Tree('leaf1'), Tree('leaf2')]), Tree('leaf3')])

    assert count_leaves(test_tree) == 3

def test_count_leaves_1_deep_leaf():
    test_tree = Tree('node1',
                    [
                        Tree('node2',
                            [
                                Tree('node3',
                                    [
                                        Tree('leaf')
                                    ]
                                )
                            ]
                        )
                    ]
                )

    print(test_tree)

    assert count_leaves(test_tree) == 1


def test_double_tree_0():
    test_tree = Tree(0)

    assert double_tree(test_tree) == Tree(0)

def test_double_tree_1():
    test_tree = Tree(1)

    assert double_tree(test_tree) == Tree(2)

def test_double_tree_4():
    test_tree = Tree(4)

    assert double_tree(test_tree) == Tree(8)

def test_double_tree_2_multiple():
    test_tree = Tree(2, [Tree(2)])

    double_tree(test_tree)
    assert test_tree == Tree(4, [Tree(4)])
    assert test_tree != Tree(4)
    assert test_tree != Tree(4, [Tree(1)])
    assert test_tree != Tree(4, [Tree(1, [Tree(4)])])


def test_count_path():
    test_tree = Tree(1)
    assert count_paths(test_tree, 1) == 1

def test_count_path_two_nodes():
    test_tree = Tree(1, [Tree(1)])
    assert count_paths(test_tree, 1) == 1

def test_count_path_three_nodes():
    test_tree = Tree(0, [Tree(1), Tree(1)])
    assert count_paths(test_tree, 1) == 2

def test_count_path_4_nodes():
    test_tree = Tree(0, [Tree(1), Tree(0, [Tree(1)])])
    assert count_paths(test_tree, 1) == 2


def test_large_tree():
    test_tree = Tree(3, [Tree(-1), Tree(1, [Tree(2, [Tree(1)]), Tree(3)]), Tree(1, [Tree(-1)])])
    assert count_paths(test_tree,3) == 2
    assert count_paths(test_tree,4) == 2
    assert count_paths(test_tree,5) == 0
    assert count_paths(test_tree,6) == 1
    assert count_paths(test_tree,7) == 2