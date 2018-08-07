import graph2015

class TestGraph:
    def setUp(self):
        self.gr = {'A': ['B', 'C'],
              'B': ['A', 'C', 'D', 'E'],
              'C': ['A', 'B', 'D'],
              'D': ['B', 'C', 'E', 'F'],
              'E': ['B', 'D', 'F', 'G', 'H'],
              'F': ['D', 'E', 'H'],
              'G': ['E', 'H', 'I'],
              'H': ['E', 'F', 'G', 'I'],
              'I': ['G', 'H']
              }
        self.graph = graph2015.Graph()
        for from_vertex, to_vertices in self.gr.iteritems():
            for to_vertex in to_vertices:
                self.graph.add_edge(from_vertex, to_vertex)

    def testbfs(self):
        print "doing bfs from A"
        self.graph.bfs('A')
    
    def testdfs(self):
        print "dfs"
        self.graph.dfs()

