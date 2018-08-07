import sys
sys.path.append("../queues")
from queue import Queue

class Enum:
    infinity = sys.maxint
    previous = None
    white = 0
    gray = 1
    black = 2
    discoverytime = None
    finishtime = None

class BFSMarker:
    def __init__(self, distance, previous, color):
        self.distance = distance
        self.previous = previous
        self.color = color

class DFSMarker:
    def __init__(self, discoverytime, finishtime, previous, color):
        self.discoverytime = discoverytime
        self.finishtime = finishtime
        self.previous = previous
        self.color = color
            
class Graph:
    def __init__(self):
        self.graph = {}
        self.bfsmarker = {}
        self.dfsmarker = {}
        self.time = None

    def add_edge(self, from_vertex, to_vertex):
        if self.graph.get(from_vertex):
            self.graph[from_vertex].append(to_vertex)
        else:
            self.graph[from_vertex] = []
            self.graph[from_vertex].append(to_vertex)
        
    def bfs(self, s):
        for vertex in self.graph:
            self.bfsmarker[vertex] = BFSMarker(Enum.infinity, Enum.previous, Enum.white)
        q = Queue()
        q.enqueue(s)
        ss = self.bfsmarker[s]
        ss.color = Enum.gray
        ss.distance = 0
        print ss.previous, s, ss.distance
        while not q.isempty():
            u = q.dequeue()
            uu = self.bfsmarker[u]
            for v in self.graph[u]:
                vv = self.bfsmarker[v]
                if vv.color == Enum.white:
                    vv.color = Enum.gray
                    vv.previous = u
                    vv.distance = uu.distance + 1
                    print vv.previous, v, vv.distance
                    q.enqueue(v)
            uu.color = Enum.black
        
    def dfs(self):
        for vertex in self.graph:
            self.dfsmarker[vertex] = DFSMarker(discoverytime=Enum.discoverytime,
                                               finishtime=Enum.finishtime,
                                               color=Enum.white,
                                               previous=Enum.previous)
        self.time = 0
        for vertex in self.graph:
            uu = self.dfsmarker[vertex]
            if uu.color == Enum.white:
                self.dfs_visit(vertex)
                    
    def dfs_visit(self, u):
        uu = self.dfsmarker[u]
        uu.color = Enum.gray
        self.time += 1
        uu.discoverytime = self.time
        print u, uu.discoverytime, uu.color
        
        for v in self.graph[u]:
            vv = self.dfsmarker[v]
            if vv.color == Enum.white:
                vv.previous = u
                self.dfs_visit(v)
        uu.color = Enum.black
        self.time += 1
        uu.finishtime = self.time
        

                
