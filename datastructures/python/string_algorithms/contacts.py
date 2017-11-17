import string


letter_position = {letter: number
                   for number, letter in enumerate(string.lowercase)}
position_letter = [letter for letter in string.lowercase]


class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = [0 for _ in range(26)]

    def str_rep(self):
        print self.data
        for number, node1 in enumerate(self.children):
            if node1:
                print position_letter[number]
                print node1.str_rep()


class Trie(object):
    def __init__(self):
        self.trie = Node('#')

    def add(self, word):
        node = self.trie
        for letter in word:
            if not node.children[letter_position[letter]]:
                #print letter, 'is not present'
                node1 = Node(False)
                node.children[letter_position[letter]] = node1
                node = node1
            else:
                #print letter, 'is present'
                node1 = node.children[letter_position[letter]]
                node = node1
        node.data = True


    def find(self, word):
        node = self.trie
        present = True
        for letter in word:
            if not node.children[letter_position[letter]]:
                #print letter, 'is not present'
                present = False
                break
            else:
                #print letter, 'is present'
                node1 = node.children[letter_position[letter]]
                node = node1
        if present:
            return self.number_of_children(node)
        else:
            return 0

    def number_of_children(self, node):
        count = 0
        if node.data == True:
            count += 1
        for child_node in node.children:
            if isinstance(child_node, Node):
                count += self.number_of_children(child_node)
        return count

    def str_rep(self):
        node = self.trie
        node.str_rep()

    
#trie = Trie()
#trie.add('hack')
#print trie.str_rep()
#trie.add('hackerrank')
#trie.str_rep()

#print trie.find('hac')
#print trie.find('hak')
trie = Trie()
n = int(raw_input().strip())
for a0 in xrange(n):
    op, contact = raw_input().strip().split(' ')
    if op == 'add':
        trie.add(contact)
    if op == 'find':
        print trie.find(contact)
