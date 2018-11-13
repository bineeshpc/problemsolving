"""
Nim is a 2 player game where the objective is to leave the 
opponent with no remaining good moves

ie if I am left with 1 coin with my turn to move I lose

So my objective is to leave 1 coin for the opponent
"""

import random

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
    NotComputed = -1
    BadPosition = -2
    position_cache = [NotComputed for i in range(remaining_coins)]
    def is_bad_position_dp_helper(remaining_coins):
        return find_good_move_dp_helper(remaining_coins) == NoGoodMove

    def find_good_move_dp_helper(remaining_coins):
        if remaining_coins == 1:
            position_cache[remaining_coins-1] = BadPosition
            return NoGoodMove
        else:
            if position_cache[remaining_coins-1] == BadPosition:
                return NoGoodMove
            elif position_cache[remaining_coins-1] != NotComputed:
                return position_cache[remaining_coins-1]
            else:
                # not computed and it should be computed now
                for picked in range(1, 4): # 1, 2, 3
                    changed_remaining_coins = remaining_coins - picked
                    if is_bad_position_dp_helper(changed_remaining_coins):
                        position_cache[remaining_coins-1] = picked
                        return picked
                position_cache[remaining_coins-1] = BadPosition 
                return NoGoodMove
    return find_good_move_dp_helper(remaining_coins)

class Player:
    def __init__(self, num):
        self.num = num
        self.choices = []
        self.is_winner = self.will_i_win()

    def will_i_win(self):
        if find_good_move_dp(self.num) == NoGoodMove:
            return False
        else:
            return True

    def play(self, num):
        move = find_good_move_dp(num)
        if move == NoGoodMove:
            move = random.choice([1, 2, 3])
            if num == 1:
                move = 1
        self.choices.append((num, move))
        remaining_num = num - move
        return remaining_num

def toggle_player(player, player1, player2):
    if player == player1:
        return player2
    else:
        return player1

def main():
    n = random.randint(1, 199)
    n1 = n
    player1 = Player(n)
    n1 = player1.play(n1)
    player2 = Player(n1)
    player = player2
    while n1 > 0:
        n1 = player.play(n1)
        player = toggle_player(player, player1, player2)

    print(player1.is_winner, player2.is_winner)
    print(player1.choices)
    print(player2.choices)

main()


        


