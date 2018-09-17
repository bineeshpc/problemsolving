import six

def permutation_without_replacement(chosen, available):
    """
    Permutation without replacement
    meaning if an item is selected once we cannot select the same item again
    0th position in n ways
    1st position in n - 1 ways
    2nd position in n - 2 ways
    ...
    ...
    kth position in n - k ways

    n-1 th position in 1 way

    there will be n! permutations
    in n = 3
    3 * 2 * 1 = 6 permutations

    """
    if len(available) == 0:
        six.print_(chosen)
    else:
        for i in range(len(available)):
            # since we dont want the same elements to be
            # repeated again and again
            # we remove the particular element from the list
            # generate a new list for further exploration
            available_after_ith_element_removed = available[0:i] + available[i+1:]
            # we chose the element here
            chosen.append(available[i])
            # explore the remaining elements and chose the rest
            # of the elements
            permutation_without_replacement(chosen, available_after_ith_element_removed)
            # we unchose the element here to prevent the 
            # list from growing
            chosen.pop()

def permutation_with_replacement(chosen, available):
    """
    This version using permutation with replacement
    After every element is chosen we assume that
    we replace the chosen back in the available to be chosen
    later

    Consider the example of natural numbers

    111 is a permutation where 1 repeats
    In this case for n positions
    we have n ^ n permutations where n is the size of available

    """

    if len(chosen) == len(available):
        six.print_(chosen)
    else:
        for i in available:
            # we chose an element
            chosen.append(i)
            # explore the rest of the possibilities with
            # a decision tree like approach
            permutation_with_replacement(chosen, available)
            # unchose the element
            # so that after exploring we can reduce the size of 
            # the element by one
            # for further exploration
            chosen.pop()
        

def main():
    lst = list('ABC')
    six.print_('Without replacement')
    permutation_without_replacement([], lst)
    six.print_('With replacement')
    permutation_with_replacement([], [0,1,2])

if __name__ == '__main__':
    main()