
NoGoodMove = None

def is_bad_position(remaining_coins):
    return find_good_move(remaining_coins) == NoGoodMove


def find_good_move(remaining_coins):
    if remaining_coins == 1:
        # base case
        return NoGoodMove
    else:
        # recursive case
        for picked in range(1, 4):
            if is_bad_position(remaining_coins - picked):
                return picked
        return NoGoodMove

for i in range(1, 30):
    print i, find_good_move(i)

