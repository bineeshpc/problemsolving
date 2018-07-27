import quicksort
import shuffle

def quickselect(a, rank):
    """
    Select the rank th smallest element from the list
    """
    def quickselect_helper(a, p, r, rank):
        if p <= r:
            q = quicksort.partition(a, p, r)
            if q == (rank - 1):
                return a[q]
            elif (rank - 1) < q:
                return quickselect_helper(a, p, q - 1, rank)
            elif (rank - 1) > q:
                return quickselect_helper(a, q + 1, r, rank)

    return quickselect_helper(a, 0, len(a) - 1, rank)


if __name__ == '__main__':

    for i in range(1, 11):
        a = shuffle.knuth_shuffle(range(1, 11))
        print quickselect(a, i)
