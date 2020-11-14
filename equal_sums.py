# Isabella Gomez A15305555
# ECE143 HW7

import numpy as np
from itertools import chain, combinations

def get_min_split(seq):
    '''
    This function takes in a sequence(set) and divides it into two subsets such that
    the sum of the subsets has the minimum possible difference between them.

    :param seq: set of unique numbers
    :return: difference between subsets
    '''

    # check that seq is a list of unique numbers
    assert (type(seq) == list or type(seq) == np.ndarray)
    if type(seq) == list:
        for i in range(len(seq)):
            assert type(seq[i]) == int
    else:
        assert issubclass(seq.dtype.type, np.integer)
        # convert numpy array to list
        seq = seq.tolist()

    # find the minimum difference between the subsets
    minimum_difference = min_diff(seq, len(seq), 0, sum(seq))

    # list with final sets
    final_subsets = []
    subsets = list(chain.from_iterable(combinations(seq, r) for r in range(1, len(seq) + 1)))
    for num in range(len(subsets) // 2):
        s1 = set(subsets[num])
        s2 = set(seq) - s1
        # check if the difference is equal to the minimum
        if abs(sum(s1) - sum(s2)) == minimum_difference:
            final_subsets.append((sorted(list(s1)), sorted(list(s2))))
    return final_subsets[::-1]

def min_diff(seq, length, calculated_sum, total_sum):
    '''
    This method find the minimum difference in the seq

    :param seq: list of unique positive ints
    :param length: length of sequence
    :param calculated_sum:
    :param total_sum:
    :return: minimum difference int
    '''

    if length == 0:
        return abs((total_sum - calculated_sum) - calculated_sum)

    # returns the minimum difference between two subsets
    return min(min_diff(seq, length - 1, calculated_sum + seq[length - 1], total_sum),
            min_diff(seq, length - 1, calculated_sum, total_sum))

