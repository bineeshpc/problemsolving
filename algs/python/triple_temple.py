"""
mma decides to visit Kodungallur temple, Triprayar temple and
Guruvayur temple.

She has to keep equal number of flowers in all the 3 temples.
As soon as she enters the temple the number of flowers in her hand
triples.
After she visits all the 3 temples she should not have any flowers
remaining.
What is the minimum number of flowers she should carry?

Atheists's answer:

comes with 0 flowers to Kodungallur temple
triples 0 to 0, keeps 0 flowers, remaining 0
comes with 0 flowers to Triprayar temple
triples 0 to 0, keeps 0 flowers, remaining 0
comes with 0 flowers to Guruvayur temple
triples 0 to 0, keeps 0 flowers, remaining 0
 
Since Amma is not an atheist what is the correct answer?
Number of flowers should be a whole number.

⁠⁠⁠Valid solutions to that problem. Infinite solutions. But 0 and 13 are the first and second elements.
⁠⁠⁠0 0
13 27
26 54
39 81
52 108
65 135
78 162
91 189
104 216
117 243
130 270
143 297
156 324
169 351
182 378
195 405

"""
def triple(x):
    return 3 * x

def put(what_i_have, what_i_put):
    return what_i_have - what_i_put

def find_solution(what_i_have, what_i_put):
    for i in range(3):
        print "before tripling", what_i_have
        what_i_have = triple(what_i_have)
        print "after tripling", what_i_have
        what_i_have = put(what_i_have, what_i_put)
        print "what i put", what_i_put
        print "remainging after putting", what_i_have
    return what_i_have == 0

def one_third(x):
    if x % 3 == 0:
        return x / 3
    else:
        return -1
    
def find_sol(what_i_have, what_i_put, count=3):
    if count == 1:
        #print what_i_have, what_i_put
        return what_i_have, what_i_put
    by3 = one_third(what_i_have)
    if by3 == -1:
        return False
    else:
        return find_sol(by3 + what_i_put, what_i_put, count-1)
        


for i in range(1000):
    ps = find_sol(i, i)
    if ps and one_third(ps[0]) != -1:
        print ps[0]/3, ps[1]

#find_solution(13, 27)
