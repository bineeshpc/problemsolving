class A:
    pass

class B:
    def set_a(self, a):
        self._a = a
        
    def get_a(self):
        return self._a

class WrongAge(Exception):
    pass

class C:

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, a):
        if a >= 0:
            self._age = a
        else:
            raise WrongAge()
            
 
def main():
    A()
    b = B()
    b.set_a(1)
    print(b.get_a())
    c = C()
    c.age = 2
    print(c.age)
    c.age = -2
    
if __name__ == '__main__':
    main()