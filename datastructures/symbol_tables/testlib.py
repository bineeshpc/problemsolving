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
