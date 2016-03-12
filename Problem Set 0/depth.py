# Python program that finds the depth of an expression.
# One way to measure the complexity of a mathematical expression is the depth of the expression
# describing it in Python lists


def depth(expression):

    if not isinstance(expression, (list, tuple)):
        return 0
    else:
        # map returns list of numbers that represent length in each branch of the expression
        # max return the max number from the list
        return max(map(depth, expression)) + 1

print depth('x')
print depth(('expt', 'x', 2))
print depth(('+', ('expt', 'x', 2), ('expt', 'y', 2)))
print depth(('/', ('expt', 'x', 5), ('expt', ('-', ('expt', 'x', 2), 1), ('/', 5, 2))))
