"""

In an American football game, a play can lead to 2 points (safety), 3 points (field goal),
or 7 points (touchdown, assuming the extra point). Many different combinations of
2, 3, and 7 point plays can make up a final score. For example, four combinations of
plays yield a score of 12:
 6 safeties (2x6 = 12),
 3 safeties and 2 field goals (2x3 + 3x2 = 12),
 1 safety, 1 field goal and 1 touchdown (2xl + 3xl + 7xl = 12), and
 4 field goals (3x4 = 12).

"""

class Football:
    def __init__(self):
        self.count = 0
        self.remember_set = set()

    def generate_ways(self, n, chosen, available):
        """
        basecase
        find success print result
        choose
        I can choose 7, 3 or 2 at every stage
        can I proceed further?
        unchoose
        """
        if (n == 0):
            composition = tuple(sorted(chosen))
            if composition not in self.remember_set:
                print composition
                self.remember_set.add(composition)
                self.count += 1
        elif n < 0:
            return None # No further evaluation possible
        else:
            # chose element 
            for value in available:
                chosen.append(value)
                index = len(chosen) - 1
                self.generate_ways(n-value, chosen, available)
                chosen.pop(index)


    def get_num_ways(self, n):
        self.value = n
        self.generate_ways(n, [], [2, 3, 7])
        print self.count


for i in range(20):
    print i
    Football().get_num_ways(i)
    print
    print


