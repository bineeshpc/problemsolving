from collections import defaultdict
import six
import sys
import StringIO
sys.path.append("../queues/")
sys.path.append("../stacks/")
sys.path.append("../linked_list")
from linkedlist import List
from queue import QueueList
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
            
        elif isiterable(V):
            self.num_vertices = int(V.readline())
            for i in range(self.num_vertices):
                self.__addvertex__(i)
            num_edges = int(V.readline())
            for _ in range(num_edges):
                v, w = V.readline().split()
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
        sio = StringIO.StringIO()
        sio.write(str(self.V()) + " vertices, ")
        sio.write(str(self.E()) + " edges\n")
        for v in range(self.V()):
            sio.write("{} : ".format(v))
            for w in self.adj(v):
                sio.write(" {}".format(w))
            sio.write("\n")
        return sio.getvalue()
        

class DFS:
    def __init__(self):
        pass
    
    def dfs(self, G, vertex):
        self.visited = {vertex:False for vertex in range(G.V())}
        self.__dfs_helper__(G, vertex)

    def __dfs_helper__(self, G, vertex):
        self.visited[vertex] = True
        for to_vertex in G.adj(vertex):
            if self.visited[to_vertex] == False:
                self.__dfs_helper__(G, to_vertex)

    def print_visited_vertices(self, G):
        for v in range(G.V()):
            if(self.visited[v]):
                print(str(v) + " "),
        six.print_()
        


class BFS:
    def __init__(self):
        pass
        
    def bfs(self, G, vertex):
        self.visited = {vertex:False for vertex in range(G.V())}
        q = QueueList()
        self.visited[vertex] = True
        q.put(vertex)
        while not q.isempty():
            v = q.get()
            for w in G.adj(v):
                if self.visited[w] == False:
                    self.visited[w] = True
                    q.put(w)


    def print_visited_vertices(self, G):
        for v in range(G.V()):
            if(self.visited[v]):
                print(str(v) + " "),
        six.print_()

                
def test_graph():
    g = Graph(sys.stdin)
    print(g)
    d = DFS()
    d.dfs(g, 0)
    d.print_visited_vertices(g)
    b = BFS()
    b.bfs(g, 9)
    b.print_visited_vertices(g)

if __name__ == '__main__':
    test_graph()
