import sys

class Node(object):
    def __init__(self, data):
        self.data = data
        self.wordcount = 1
        self.children = {}

    def str_rep(self):
        print self.data, self.wordcount
        for letter, node1 in self.children.iteritems():
            if node1:
                print letter
                print node1.str_rep()


class Trie(object):
    def __init__(self):
        self.trie = Node('#')
        self.trie.wordcount = 0   # set this to 0 initially because it contains only root node
        # root node is not considered as a word

    def add(self, word):
        node = self.trie
        for letter in word:
            if not node.children.get(letter):
                # print "add ", letter, 'is not present'
                node1 = Node(False)
                node.children[letter] = node1
                node = node1
            else:
                # print "add ", letter, 'is present'
                node1 = node.children[letter]
                node1.wordcount += 1
                node = node1
        node.data = True
        self.trie.wordcount += 1

    def find_recursive(self, word):
        """ Find using recursive function"""
        node = self.trie
        present = True
        for letter in word:
            if not node.children.get(letter):
                # print letter, 'is not present'
                present = False
                break
            else:
                # print letter, 'is present'
                node1 = node.children[letter]
                node = node1
        if present:
            return self.number_of_children(node)
        else:
            return 0


    def find(self, word):
        """ Find using dynamic programming """
        node = self.trie
        present = True
        for letter in word:
            if not node.children.get(letter):
                # print "find ", letter, 'is not present'
                present = False
                break
            else:
                # print "find ", letter, 'is present'
                node1 = node.children[letter]
                node = node1
        if present:
            return node.wordcount
        else:
            return 0

    def number_of_children(self, node):
        count = 0
        if node.data:
            count += 1
        for letter, child_node in node.children.iteritems():
            count += self.number_of_children(child_node)
        return count

    def str_rep(self):
        node = self.trie
        node.str_rep()


trie = Trie()
n = int(raw_input().strip())
count = 0
for a0 in xrange(n):
    op, contact = raw_input().strip().split(' ')
    if op == 'add':
        trie.add(contact)
    elif op == 'find':
        if count == 0:
            sys.stdout.write('{}'.format(trie.find(contact)))
            count += 1
        else:
            sys.stdout.write('\n{}'.format(trie.find(contact)))

# print trie.str_rep()
