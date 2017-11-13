class Perm:
    def __init__(self, b):
        self.values = []
        self.options = b
        self.a = [i for i in b]
        self.used = {i:False for i in self.a}
        
        
    def generate_perm_with_replacement(self, n):
        if n <= 0:
            d = self.a[:]
            self.values.append(d)
        else:
            for c in self.options:
                self.a[n-1] = c
                self.generate_perm_with_replacement(n-1)
                #print a, n
                
    def generate_perm(self, n): 
        if n <= 0:
            d = self.a[:]
            self.values.append(d)
            
            
        else:
            for c in self.options:
                #if c not in self.a[n:]:
                if self.used[c] == False:
                    self.used[c] = True
                    self.a[n-1] = c
                    
                    self.generate_perm(n-1)
                    self.used[c] = False


