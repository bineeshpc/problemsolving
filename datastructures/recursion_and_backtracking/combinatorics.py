class Perm:
    def __init__(self, choices):
        self.permutations = []
        self.choices = choices
        self.choices_list = [choice  for choice in choices]
        self.used = {choice:False for choice in self.choices_list}
        
        
    def generate_perm_with_replacement(self, n):
        if n <= 0:
            self.permutations.append([i for i in self.choices_list])
        else:
            for choice in self.choices:
                # n-1 th place can be filled in len(choices_list) ways
                # n-2 the  can be filled in len(choices_list) ways and so on
                self.choices_list[n-1] = choice  # make this choice for n-1
                # rely on recursion to generate from n-1 to 0
                self.generate_perm_with_replacement(n-1)
                
                
    def generate_perm(self, n): 
        if n <= 0:
            self.permutations.append([i for i in self.choices_list])
        else:
            for choice in self.choices:
                if self.used[choice] == False:
                    # choose, explore, unchoose pattern in backtracking
                    self.used[choice] = True  # remember the choice
                    self.choices_list[n-1] = choice
                    self.generate_perm(n-1)
                    self.used[choice] = False # unchoose

def example_usage1(str1):
    p = Perm(str1)
    p.generate_perm(len(str1))
    return p.permutations

def example_usage2(str1):
    p = Perm(str1)
    p.generate_perm_with_replacement(len(str1))
    return p.permutations


if __name__ == '__main__':
    print(sorted(example_usage1("abc")))
    print(sorted(example_usage2("abc")))
