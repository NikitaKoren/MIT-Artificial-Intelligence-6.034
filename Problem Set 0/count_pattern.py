# python program which counts the number of times a certain pattern of symbols appears in a list, including overlaps
# Example:
# count_pattern( ('a', 'b'), ('a','b', 'c', 'e', 'b', 'a', 'b', 'f')) should return 2
# count_pattern((('a', 'b', 'a'), ('g', 'a', 'b', 'a', 'b', 'a','b', 'a'))) should return 3


def count_pattern(exp):

    pattern_length = len(exp[0])
    list_length = len(exp[1])

    pattern_count = 0

    # iterate through the lists and count pattern matches
    list_iterator = 0
    while list_iterator < list_length and list_iterator + pattern_length <= list_length:

        # if the fist char of a pattern was found, continue to check; otherwise skip
        pattern_iterator = 0
        if exp[0][pattern_iterator] == exp[1][list_iterator]:

            # iterate through a pattern
            while pattern_iterator < pattern_length and exp[0][pattern_iterator] == exp[1][list_iterator]:
                pattern_iterator += 1
                list_iterator += 1

            # if after the loop pattern iterator reached the end, the pattern was found
            if pattern_iterator == pattern_length:
                pattern_count += 1
                # back one position to check overlaps
                list_iterator -= 1
        else:
            list_iterator += 1

    return pattern_count



# test program
print "The output should be 0 1 2 3 4"

print "Output: "
print count_pattern((('z', 'b', 'a', 'c'), ('g', 'a', 'b', 'a', 'c', 'a','b', 'a')))
print count_pattern((('a', 'b', 'a', 'c'), ('g', 'a', 'b', 'a', 'c', 'a','b', 'a')))
print count_pattern((('a', 'b'), ('a', 'b', 'c', 'e', 'b', 'a', 'b', 'f')))
print count_pattern((('a', 'b', 'a'), ('g', 'a', 'b', 'a', 'b', 'a','b', 'a', 'b')))
print count_pattern((('a', 'b'), ('a', 'b', 'a', 'b', 'a', 'b', 'a', 'b')))




