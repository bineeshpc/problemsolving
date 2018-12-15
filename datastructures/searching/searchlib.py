def binary_search(a, n):
    """
    Will work on sorted arrays in logarithmic time
    Returns none if element is not found
    Returns the index if the element is found
    """
    def binary_search_helper(a, begin, end, n):
        if begin > end:
            return None
        mid = (begin + end) // 2
        if a[mid] == n:
            return mid
        else:
            if n < a[mid]:
                return binary_search_helper(a, begin, mid - 1, n)
            if n > a[mid]:
                return binary_search_helper(a, mid + 1, end, n)

    def binary_search_helper_itr(a, begin, end, n):
        while begin <= end:
            mid = (begin + end) // 2
            if a[mid] == n:
                return mid
            else:
                if n < a[mid]:
                    end = mid - 1
                elif n > a[mid]:
                    begin = mid + 1
        return None

    return binary_search_helper_itr(a, 0, len(a) - 1, n)



def linear_search(a, n):
    """ Will work on all arrays in linear time
    Returns none if element is not found
    Returns the index if the element is found
    """

    i = 0
    length = len(a)
    while i < length:
        if a[i] == n:
            return i
        i += 1
    return None
