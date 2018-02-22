def move_disk(source, destination, n):
    print 'Moving disk {n} from {source} to {destination} '.format(n=n, source=source, destination=destination)

def towers_of_hanoi(source, destination, temp, n):
    """ 
    Towers of hanoi problem

    1
    2
    3
    4
    5
    6

    """

    # base case
    # only 1 disk
    # move 1 disk from source to destination
    if n == 1:
        move_disk(source, destination, n)
    # recursive case
    # move n - 1 disks from source to temp
    # move nth disk from source to destination
    # move n - 1 disks from temp to destination
    else:
        towers_of_hanoi(source, temp, destination, n - 1)
        move_disk(source, destination, n)
        towers_of_hanoi(temp, destination, source, n - 1)

towers_of_hanoi('A', 'B', 'C', 3)
