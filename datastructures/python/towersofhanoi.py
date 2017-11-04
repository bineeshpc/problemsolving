import traceback

def move(height, ft, tt):
    print "Moving disk {} from {} to {}".format(height, ft, tt)

def towersofhanoi(height, fromone, withone, toone):
    #traceback.print_stack()
    if height > 0:
        towersofhanoi(height - 1, fromone, toone, withone)
        move(height, fromone, toone)
        towersofhanoi(height - 1, withone, fromone, toone)

towersofhanoi(2, "A", "B", "C")

