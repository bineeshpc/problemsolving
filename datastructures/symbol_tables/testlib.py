import random
import BST

def test_SequentialSearchST(st):
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

def test_BinarySearchST(st):
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
        assert st.check() == True
        assert st.size() == (i + 1)
        assert st.get(i) == i
        
    
    expected_keys = list([(i, i) for i in range(10)])
    actual_keys = [(key, value) for key, value in st]
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


def test_BST(st):
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
        assert st.check() == True
        assert st.size() == (i + 1)
        assert st.height() == (i + 1)
        assert st.floor(i) == i
        st.in_order()
        assert st.get(i) == i
        
    
    expected_keys = list([(i, i) for i in range(10)])
    actual_keys = [(node.key, node.value) for node in st.in_order()]
    assert expected_keys == actual_keys
    assert st.check() == True

    for i in range(10):
        assert st.get(i) == i
        st.put(i, i+1)

        assert st.get(i) == i+1
        assert st.contains(i) == True
        st.delete(i)
        assert st.contains(i) == False
        assert st.get(i) == None   

    assert st.isempty() == True


    rand_ints = [random.randint(1, 1000) for _ in range(50)]
    rand_ints_expected = sorted(set((i, i) for i in rand_ints))
    for i in rand_ints:
        st.put(i, i)
    rand_ints_actual = [(node.key, node.value) for node in st.in_order()]
    # print(list(zip(rand_ints_expected, rand_ints_actual)))
    assert rand_ints_expected == rand_ints_actual
            

def pre_order(st, lst):
    if st:
        lst.append(st.key)
        pre_order(st.left, lst)
        pre_order(st.right, lst)
    return lst
    

def in_order(st, lst):
    if st:
        in_order(st.left, lst)
        lst.append(st.key)
        in_order(st.right, lst)
    return lst


def post_order(st, lst):
    if st:
        post_order(st.left, lst)
        post_order(st.right, lst)
        lst.append(st.key)
    return lst


def test_BST_delete(st):
    assert pre_order(st.root, []) == []
    add_order = [5, 4, 6, 10]
    for i in add_order:
        st.put(i, i)
    
    assert pre_order(st.root, []) == [5, 4, 6, 10]
    assert in_order(st.root, []) == [4, 5, 6, 10]
    assert post_order(st.root, []) == [4, 10, 6, 5]

    st.delete(5)
    assert pre_order(st.root, []) == [6, 4, 10]
    assert in_order(st.root, []) == [4, 6, 10]
    assert post_order(st.root, []) == [4, 10, 6]