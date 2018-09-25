import sys

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class SequentialSearchST:
    def __init__(self):
        self.head = None
        self.count = 0

    def put(self, key, value):       
        # check for presence of key
        # and replace it with new value
        node = self.head
        while node != None:
            if node.key == key:
                node.value = value
                return
            node = node.next
        # key was not found
        # in the symbol table
        # add the key, value pair
        node = Node(key, value)
        node.next = self.head
        self.head = node
        self.count += 1

    def get(self, key):
        node = self.head
        while node != None:
            if node.key == key:
                return node.value
            node = node.next
        return None

    def contains(self, key):
        node = self.head
        while node != None:
            if node.key == key:
                return True
            node = node.next
        return False

    def __iter__(self):
        self.iterhelper = self.head
        return self

    def __next__(self):
        node = self.iterhelper
        if node == None:
            raise StopIteration
        else:
            self.iterhelper = node.next
            return node

    def size(self):
        return self.count

    def isempty(self):
        return self.count == 0

    def delete(self, key):
        if self.head:
            if self.head.key == key:
                self.head = None
                self.count -= 1
            else:
                previous_node = self.head
                node_to_delete = previous_node.next
                while node_to_delete != None:
                    if node_to_delete.key == key:
                        previous_node.next = node_to_delete.next
                        self.count -= 1
                    previous_node = node_to_delete
                    node_to_delete = node_to_delete.next
            

def main():
    st = SequentialSearchST()
    assert st.isempty() == True
    assert st.get('A') == None
    st.put('A', 1)
    assert st.size() == 1
    st.get('A') == 1
    assert st.isempty() == False
    st.delete('A')
    assert st.contains('A') == False
    assert st.get('A') == None
    assert st.isempty() == True
    assert st.size() == 0

    for i in range(10):
        assert st.get(i) == None
        st.put(i, i)
        assert st.size() == (i + 1)
        assert st.get(i) == i

    
    expected_keys = list([(i, i) for i in range(10)])
    actual_keys = [(node.key, node.value) for node in st]
    actual_keys.sort()
    assert expected_keys == actual_keys

    for i in range(10):
        assert st.get(i) == i
        st.put(i, i+1)
        assert st.get(i) == i+1
        assert st.contains(i) == True
        st.delete(i)
        assert st.contains(i) == False
        assert st.get(i) == None   

    assert st.isempty() == True

if __name__ == '__main__':
    main()