def move(height, from_rod, to_rod):
    """ To move disk with height x from from rod to to rod
    Args: height of the rod from rod and to rod
    Returns: None """
    print "Moving disk {} from {} to {}".format(height, from_rod, to_rod)

def towersofhanoi(height, from_rod, with_rod, to_rod):
    """ Function to solve towersofhanoi 
    Args: height of the rod
    from_rod with_rod to_rod"""
    if height > 0:
        towersofhanoi(height - 1, from_rod, to_rod, with_rod)
        move(height, from_rod, to_rod)
        towersofhanoi(height - 1, with_rod, from_rod, to_rod)

towersofhanoi(6, "A", "B", "C")
