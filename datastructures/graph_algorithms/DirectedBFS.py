import DiGraph
import six
import sys
sys.path.append("../queues/")
from queue import QueueList

class DirectedBFS:
    def __init__(self, G, vertex):
        self.bfs(G, vertex)
        
    def bfs(self, G, vertex):
        self.visited = [False for v in range(G.V())]
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


def test_BFS():
    g = DiGraph.DiGraph("tests/tinyG.txt")
    print(g)
    b = DirectedBFS(g, 0)
    b.print_visited_vertices(g)


if __name__ == '__main__':
    test_BFS()