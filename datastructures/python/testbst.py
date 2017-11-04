from nose.tools import with_setup
import bst
import random

class TestBst:
    def setUp(self):
        self.elements = [100]
        self.bst_node = bst.Node(self.elements[0])
        for i in range(20):
            el = random.randint(0,200)
            self.bst_node.insert(el)
            self.elements.append(el)


    def test_preorder(self):
        print "Preorder :",
        self.bst_node.preorder()
        print
        
    def test_inorder(self):
        print "Inorder  :",
        self.bst_node.inorder()
        print
        
    def test_postorder(self):
        print "Postorder:",
        self.bst_node.postorder()
        print
        
    def test_checkpresence(self):
        for i in range(5):
            el = random.choice(self.elements)
            print el, self.bst_node.checkpresence(el)
            el = random.randint(300, 400)
            print el, self.bst_node.checkpresence(el)
            
    def test_commonroot(self):
        el1, el2 = [random.choice(self.elements) for i in range(2)]
        cr = bst.CommonRoot(el1, el2)
        print self.bst_node.getcommonroot(cr), cr.elements
        
    def testmax(self):
        print "Inorder  :",
        self.bst_node.inorder()
        print        
        print "Max is ", self.bst_node.findmax()
        print "Max is ", self.bst_node.findmaxlevelorder()
        
    def testsize(self):
        bstnode = bst.Node(random.randint(1, 100))
        for _ in range(19):
            el = random.randint(1, 10)
            bstnode.insert(el)
        print "size is", bstnode.size()
        
    def testheight(self):
        bstnode = bst.Node(random.randint(1, 100))
        for _ in range(19):
            el = random.randint(1, 10)
            bstnode.insert(el)
        print "height is", bstnode.height()
        
    def testmirror(self):
        print "mirroring"
        bstnode = bst.Node(random.randint(1, 100))
        for _ in range(19):
            el = random.randint(1, 10)
            bstnode.insert(el)
        print "Inorder  :",
        bstnode.inorder()
        print
        bstnode.tomirror()
        print "Inorder  :",
        bstnode.inorder()
        print
        
    def testlca(self):
        a, b = [random.choice(self.elements) for i in range(2)]
        print "LCA", self.bst_node.leastcommonancestor(a, b)
        cr = bst.CommonRoot(a, b)
        print self.bst_node.getcommonroot(cr), cr.elements
        
    def testverticalsum(self):
        hashtable = {}
        bstnode = bst.Node(100)
        bstnode.left = bst.Node(50)
        bstnode.right = bst.Node(150)
        bstnode.verticalsum(0, hashtable)
        print "Vertical sum", hashtable