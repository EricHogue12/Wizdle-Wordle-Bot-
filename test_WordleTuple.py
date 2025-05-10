import pytest
import WordleTuple

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


    