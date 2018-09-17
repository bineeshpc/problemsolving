"""
Nim is a 2 player game where the objective is to leave the 
opponent with no remaining good moves

ie if I am left with 1 coin with my turn to move I lose

So my objective is to leave 1 coin for the opponent
"""
NoGoodMove = None

def is_bad_position(remaining_coins):
    """
    A bad position is a position where I have no good moves
    """
    return find_good_move(remaining_coins) == NoGoodMove


def find_good_move(remaining_coins):
    if remaining_coins == 1:
        # base case
        return NoGoodMove
    else:
        # recursive case
        for picked in range(1, 4):
            # since I want to put the opponent in a 
            # bad position
            # I pick the number of coins which would put
            # my opponent in a bad position
            if is_bad_position(remaining_coins - picked):
                return picked
        return NoGoodMove


def find_good_move_dp(remaining_coins):
    """ This is the dp version of the same problem
    This memoized 
    """
    is_bad_position_cache = [False for i in range(remaining_coins)]
    def is_bad_position_dp_helper(remaining_coins):
        if is_bad_position_cache[remaining_coins-1]:
            return is_bad_position_cache[remaining_coins-1]
        else:
            if find_good_move_dp_helper(remaining_coins) == NoGoodMove:
                is_bad_position_cache[remaining_coins-1] == True
                return is_bad_position_cache[remaining_coins-1]
            else:
                return False

    def find_good_move_dp_helper(remaining_coins):
        if remaining_coins == 1:
            is_bad_position_cache[0] = True
            return is_bad_position_cache[0]
        else:
            for picked in range(1, 4): # 1, 2, 3
                changed_remaining_coins = remaining_coins - picked
                if is_bad_position_dp_helper(changed_remaining_coins):
                    return picked
                        
            return NoGoodMove

for i in range(1, 30):
    print i, find_good_move(i)

