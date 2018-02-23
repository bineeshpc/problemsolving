def get_all_sublists(s):
    """
    Given a set of integers and a target value, determine whether it is
    possible to find a subset of those integers whose sum is equal to
    the specified target.

    s = { -2, 3 , 1, 8 }

    subset_sum(s, 7)==> true because of (-2, 1, 8)
    """
    def sublist_helper(chosen, available):
        # base case
        # set is empty
        if len(available) == 0:
            print chosen
        # recursive case
        # set is non empty
        # divide it into two branches
        # that includes a particular number
        # and that does not include a particular number

        else:
            # we dont need loop because we are not bothered about the arrangement
            # We only need inclusion or exclusion of a particular element
            # This can be achieved by a recursion with the element and
            # another recursion without that element
            # recursions will take care of the problems
            element = available.pop(0)
            # choose element is chosen
            # explore the subsets without this element added to chosen
            sublist_helper(chosen, available)
            # explore the subsets with this element added to chosen
            chosen.append(element)
            sublist_helper(chosen, available)
            # unchoose the element that was chosen before
            element = chosen.pop()  # takes out the last element that was chosen
            # that last element that was chosen is present in the end of the list
            available.insert(0, element)
            # insert the element back to the beginning of the available list



    sublist_helper([], s)


get_all_sublists([1, 2, 3, 4])

