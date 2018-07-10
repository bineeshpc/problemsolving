from collections import defaultdict
import sys
sys.path.append("../queues/")
from queue import QueueList

class Graph(object):
    def __init__(self):
        self.adjacencylist = defaultdict(list)

    def addvertex(self, vertex):
        self.adjacencylist.setdefault(vertex, [])

    def addedge(self, edge):
        source_vertex, target_vertex = edge
        self.adjacencylist.setdefault(source_vertex, []).append(target_vertex)

    def get_vertices(self):
        vertices = []
        for vertex in self.adjacencylist:
            vertices.append(vertex)
        return vertices

    def get_edges(self):
        vertices = self.get_vertices()
        edges = []
        for vertex in self.adjacencylist:
            for to_vertex in self.adjacencylist[vertex]:
                edges.append((vertex, to_vertex))
        return edges

    def bfs(self, vertex):
        visited = {vertex:False for vertex in self.get_vertices()}
        q = QueueList()
        visited[vertex] = True
        q.put(vertex)
        nodes_list = []
        while not q.isempty():
            node = q.get()
            nodes_list.append(node)
            for to_vertex in self.adjacencylist[node]:
                if visited[to_vertex] == False:
                    visited[to_vertex] = True
                    q.put(to_vertex)
        return nodes_list

    def dfs(self, vertex):
        visited = {vertex:False for vertex in self.get_vertices()}
        node_list = []
        def dfs_helper(self, vertex):
            visited[vertex] = True
            node_list.append(vertex)
            for to_vertex in self.adjacencylist[vertex]:
                if visited[to_vertex] == False:
                    dfs_helper(self, to_vertex)

        dfs_helper(self, vertex)
        return node_list
                
def test_graph():
    g = Graph()
    vertices = range(1, 6)
    for vertex in vertices:
        g.addvertex(vertex)

    edges = [(1, 2), (1,3), (1, 5), (2, 5), (2, 3), (2, 5)]
    for edge in edges:
        g.addedge(edge)

    print g.get_vertices()
    print g.get_edges()
    print g.bfs(1)
    print g.dfs(1)

    

test_graph()
if __name__ == '__main__':
    test_graph()
