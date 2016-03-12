# Python program that is analogous to list referencing, but for trees


def tree_ref(tree, index):
    if len(index) == 0:
        return tree
    else:

        # iterate through the current level of a tree and find needed index
        walker = 0
        while walker < index[0]:
            walker += 1

        # send needed tree branch to the next level of recursion
        return tree_ref(tree[walker], index[1:])


# Python tuple that represents tree
tree = (((1, 2), 3), (4, (5, 6)), 7, (8, 9, 10))

print tree_ref(tree, (1,1,1))
