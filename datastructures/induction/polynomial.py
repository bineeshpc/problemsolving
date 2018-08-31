import sys
import math
import six

class Polynomial:
    def __init__(self, x, n, coefficient_list):
        self.x = x
        self.n = n
        self.coefficient_list = coefficient_list
        assert len(self.coefficient_list) == self.n + 1

    def evaluate(self):
        """ Trivial implementation by using math.pow
        """
        p = self.coefficient_list[0]  # a0
        for i in range(1, self.n+1):
            ai = self.coefficient_list[i]
            p += ai * math.pow(self.x, i)
        return p

    def recursive_1(self):
        """
            Simply compute x ^ n * an + P(n-1)
        """
        def recursion_helper(n):
            if n == 0:
                return self.coefficient_list[n]
            else:
                return math.pow(self.x, n) * self.coefficient_list[n] + recursion_helper(n-1)

        return recursion_helper(self.n)


    def evaluate_2(self):
        """
            Eliminate the last co efficient first
            P(n-1)(x)  = x * [ an * x ^ (n - 1) + an-1 * x ^ (n-2) + ... a1]
            Pn(x) = P(n-1)(x) + a0
        """
        a = self.coefficient_list
        x = self.x
        n = self.n
        P = a[n]
        for i in range(1, n+1):
            P = P * x + a[n-i]

        return P

    def __str__(self):
        st = []
        for i in range(self.n, -1, -1):
            st.append('a{} x^{}'.format(i, i))
        return ' + '.join(st)



def test_polynomial(filename):
    with open(filename) as f:
        num_testcases = int(f.readline().strip())
        for _ in range(num_testcases):
            x = float(f.readline().strip())
            n = int(f.readline().strip())
            coefficient_list = [float(y) for y in f.readline().strip().split()]
            p = Polynomial(x, n, coefficient_list)
            six.print_(p)
            six.print_(p.evaluate())
            six.print_(p.recursive_1())
            six.print_(p.evaluate_2())
    
if __name__ == '__main__':
    filename = sys.argv[1]
    test_polynomial(filename)