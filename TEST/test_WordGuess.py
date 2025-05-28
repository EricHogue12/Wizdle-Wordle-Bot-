import pytest
import SRC.WordGuess as WordGuess

def test_valid_word():
    
    guess = WordGuess.WordGuess("yolol", "bybyb")
    with pytest.raises(ValueError, match="user word guess should be a real word"):
        guess.valid_word()

def test_constructor():
    # valid cases
    guess1 = WordGuess.WordGuess("slate", "bbbbb")
    assert guess1.wordS == "slate"
    assert guess1.colorS == "bbbbb"
    
    # invalid cases
    with pytest.raises(TypeError, match="user word guess should be a String"):
        WordGuess.WordGuess(True, False)
    with pytest.raises(TypeError, match="user color input should be a String"):
        WordGuess.WordGuess("dd", False)
    with pytest.raises(ValueError, match="user word guess should be 5 letters long"):
        WordGuess.WordGuess("dd", "bybyb")
    with pytest.raises(ValueError, match="user color input should be 5 letters long"):
        WordGuess.WordGuess("ddddd", "byby")
    with pytest.raises(ValueError, match="user word guess should be only letters"):
        WordGuess.WordGuess("f1fff", "bybyb")
    with pytest.raises(ValueError, match="user color input should be only letters"):
        WordGuess.WordGuess("fffff", "byb*b")
    with pytest.raises(ValueError, match="user color input should only contain the letters G -> green, Y -> yellow, or B -> black"):
        WordGuess.WordGuess("fffff", "hello")

