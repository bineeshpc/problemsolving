import graph

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
        self.graph = graph.Graph(self.gr)

    def testbfs(self):
        self.graph.bfs('A')
    
    def testdfs(self):
        self.graph.dfs()

