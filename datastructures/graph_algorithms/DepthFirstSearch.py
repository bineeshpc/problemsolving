import Graph
import six

class DFS:
    def __init__(self, G, vertex):
        self.dfs(G, vertex)
    
    def dfs(self, G, vertex):
        self.visited = [False for v in range(G.V())]
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
        

def testDFS():
    G = Graph.Graph("tests/tinyG.txt")
    print(G)
    d = DFS(G, 0)
    d.print_visited_vertices(G)

if __name__ == '__main__':
    testDFS()