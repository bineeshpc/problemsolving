"""
https://www.geeksforgeeks.org/select-a-random-node-from-a-singly-linked-list/

"""
import six
import linkedlist
import random


def select_random_node(lst):
    """
    This method used two traversals
    First traverse the list and find out the length
    of the list
    """
    count = 0
    for _ in lst:
        count += 1

    n = count
    random_element = None
    runner = lst.head.next
    
    i = 1
    while runner is not None:
        if random.randint(0, n-i) == 0:
            random_element = runner.data
        if random_element is not None:
            break
        runner = runner.next
        i += 1
    return random_element


def check_frequencies(input_data, sample_size):
    frequency = {i:0 for i in input_data}
    for _ in range(sample_size):
        value = select_random_node(input_data)
        frequency[value] += 1
    six.print_(frequency)


def main():
    lst = linkedlist.List()
    lst.createlist(range(10))
    check_frequencies(lst, 10**6)


if __name__ == '__main__':
    main()