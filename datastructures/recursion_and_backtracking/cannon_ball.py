"""
pattern of n ^ 2 elements at each level.
Based on the height return the total number of elements in the canon ball

*
****
*********
this kind of arrangement

"""


def num_canonballs(height):
    if height == 0:
        return 0
    else:
        return height * height + num_canonballs(height - 1)


for i in range(10):
    print i, num_canonballs(i)
