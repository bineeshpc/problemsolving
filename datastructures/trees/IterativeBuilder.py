
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree(n):
    """
    Build tree upto size n
    """
    nodes = []
    for i in range(1, n+1):
        nodes.append(Node(i))
    length = n // 2
    for i in range(1, length+1):
        #six.print_(i, i-1, i*2 -1, i*2)
        node = nodes[i-1]
        node.left = nodes[i * 2 - 1]
        node.right = nodes[i * 2]
    return nodes[0]
