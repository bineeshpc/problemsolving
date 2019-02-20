
def read_input():
    s1 = input()
    s2 = input()
    n, e, m = [int(i) for i in s1.split()]
    a = [int(i) for i in s2.split()]
    return n, e, m, a

def find_max(a):
    b = sorted(a, reverse=True)    
    return b[1], b[0]
            
            

def problem_b(n, e, m, a):
    sm, fm = find_max(a)
    #max_ = e // (m + 1)
    if e % (m+1) == 0:
        
        print((e//(m + 1)) * (fm * m + sm))
    else:
        num_times = e // (m + 1)
        remaining = e - num_times * (m+1)
    
        print(num_times * (fm * m + sm) + remaining * fm)
    

if __name__ == '__main__':
    n, e, m, a = read_input()
    problem_b(n, e, m, a)