from collections import defaultdict
import six
import sys
sys.path.append("../queues/")
sys.path.append("../stacks/")
sys.path.append("../linked_list")
from linkedlist import List
from stack_linked_list import Stack


def isiterable(x):
    """ Returns true if x is an iterable """
    try:
        iter(x)
        isiter = True
    except:
        isiter = False
    return isiter
    

class Graph(object):
    def __init__(self, V):
        """
        Creates a graph with v vertices
        """
        self.adjacencylist = []
        self.num_edges = 0
        if isinstance(V, int):
            for vertex in range(V):
                self.__addvertex__(vertex)
            self.num_vertices = V
            
        elif isinstance(V, str):
            with open(V) as f:
                self.num_vertices = int(f.readline())
                for i in range(self.num_vertices):
                    self.__addvertex__(i)
                num_edges = int(f.readline())
                for _ in range(num_edges):
                    v, w = f.readline().split()
                    v = int(v)
                    w = int(w)
                    self.add_edge(v, w)
            

    def __addvertex__(self, vertex):
        self.adjacencylist.append(List())

    def add_edge(self, v, w):
        self.adjacencylist[v].insert_in_beginning(w)
        self.adjacencylist[w].insert_in_beginning(v)
        self.num_edges += 1

    def V(self):
        """
        Returns number of vertices
        """
        return self.num_vertices

    
    def E(self):
        """ Returns number of edges"""
        return self.num_edges
    
    def adj(self, v):
        """ Returns an iterator of all vertices that is adjacent to v"""
        for w in self.adjacencylist[v]:
            yield w

    def __str__(self):
        """ 
        Returns the graph in string form 
        """
        sio = six.StringIO()
        sio.write(str(self.V()) + " vertices, ")
        sio.write(str(self.E()) + " edges\n")
        for v in range(self.V()):
            sio.write("{} : ".format(v))
            for w in self.adj(v):
                sio.write(" {}".format(w))
            sio.write("\n")
        return sio.getvalue()
        
                
def test_graph():
    g = Graph("tests/tinyG.txt")
    print(g)


if __name__ == '__main__':
    test_graph()
