from production import AND, OR, NOT, PASS, FAIL, IF, THEN, \
    match, populate, simplify, variables
from zookeeper import ZOOKEEPER_RULES


# This function, which you need to write, takes in a hypothesis
# that can be determined using a set of rules, and outputs a goal
# tree of which statements it would need to test to prove that
# hypothesis. Refer to the problem set (section 2) for more
# detailed specifications and examples.

# Note that this function is supposed to be a general
# backchainer.  You should not hard-code anything that is
# specific to a particular rule set.  The backchainer will be
# tested on things other than ZOOKEEPER_RULES.

# Algorithm for backward chaining:

# -  Given a hypothesis, you want to see what rules can produce it, by matching the consequents of
# those rules against your hypothesis. All the consequents that match are possible options, so you'll
# collect their results together in an OR node. If there are no matches, this statement is a leaf, so
# output it as a leaf of the goal tree.

# -  If a consequent matches, keep track of the variables that are bound. Look up the antecedent of
# that rule, and instantiate those same variables in the antecedent (that is, replace the variables with
# their values). This instantiated antecedent is a new hypothesis.

# - The antecedent may have AND or OR expressions. This means that the goal tree for the
# antecedent is already partially formed. But you need to check the leaves of that AND-OR tree,
# and recursively backward chain on them.

#  'opus is a penguin'
#                         'opus does not fly'  OR 'opus swims' OR 'opus has black and white color' AND
# 'opus is a bird'  OR 'opus has feathers'  OR 'opus flies' AND 'opus lays eggs'


def backchain_to_goal_tree(rules, hypothesis):
    goal_tree = [hypothesis]
    for rule in rules:
        # take THEN part of a rule
        consequent = rule.consequent()
        for option in consequent:
            bindings = match(option, hypothesis)
            if bindings or option == hypothesis:
                # take IF part of a rule
                antecedent = rule.antecedent()
                if isinstance(antecedent, str):
                    new_hypothesis = populate(antecedent, bindings)
                    goal_tree.append(backchain_to_goal_tree(rules, new_hypothesis))
                    goal_tree.append(new_hypothesis)
                else:
                    statements = [populate(ante_expr, bindings) for ante_expr in antecedent]
                    new_goal_tree = []
                    for statement in statements:
                        new_goal_tree.append(backchain_to_goal_tree(rules, statement))

                    # check the leaves of AND-OR tree and recursively backward chain on them.
                    if isinstance(antecedent, AND):
                        goal_tree.append(AND(new_goal_tree))
                    else:
                        goal_tree.append(OR(new_goal_tree))
    return simplify(OR(goal_tree))



# Here's an example of running the backward chainer - uncomment
# it to see it work:
# print backchain_to_goal_tree(ZOOKEEPER_RULES, 'opus is a penguin')
# print backchain_to_goal_tree(ZOOKEEPER_RULES, 'opus is a giraffe')
# print backchain_to_goal_tree(ARBITRARY_EXP, 'zot')
