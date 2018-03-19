import combinatorics

class Test:
    def testpermutationwithreplacement(self):
        
        b = "abc"
        perm = combinatorics.Perm(b)
        perm.generate_perm_with_replacement(len(b))
        print "with replacement", perm.permutations, len(perm.permutations)
        
    def testperm(self):
        b = "abc"
        perm = combinatorics.Perm(b)
        perm.generate_perm(len(b))
        print "without replacement", perm.permutations, len(perm.permutations)
