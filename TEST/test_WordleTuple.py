import pytest
import SRC.WordleTuple as WordleTuple

def test_index_of():
    wordTest = WordleTuple.WordleTuple("a", "b", "c", "d")
    assert wordTest.index_of("c") == 2

def test_getter_method():
    wordTest = WordleTuple.WordleTuple("a", "b", "c", "d")
    assert wordTest.getter_method()[0] == "a"

def test_get_item():
    wordTest = WordleTuple.WordleTuple("a", "b", "c", "d")
    assert wordTest.get_item(0) == "a"

def test_length():
    wordTest = WordleTuple.WordleTuple("a", "b", "c", "d")
    assert wordTest.length() == 4

def test_constructor():
    # invalid case
    with pytest.raises(TypeError, match="invalid list of words"):
        WordleTuple.WordleTuple(1, 2, 3, 4)
     
    # valid case
    wordTest = WordleTuple.WordleTuple("hi", "hello", "ciao")
    assert wordTest.data[0] == "hi"
    assert wordTest.data[1] == "hello"
    assert wordTest.data[2] == "ciao"
    
    
