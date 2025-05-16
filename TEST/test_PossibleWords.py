import pytest
import SRC.PossibleWords as PossibleWords
import SRC.WordGuess as WordGuess

def test_constructor():
    poss1 = PossibleWords.PossibleWords(("hello", "hi"))
    assert poss1.possible == ["hello", "hi"]
    assert len(poss1.greenletters) == 0
    assert len(poss1.greenindices) == 0
    assert len(poss1.blackletters) == 0
    assert len(poss1.blackindices) == 0

def test_update_letters():
    poss1 = PossibleWords.PossibleWords(("flock", "donut", "shale"))
    # tests for easy green and black cases
    guess1 = WordGuess.WordGuess("slate", "bgbbb")
    poss1.update_letters(guess1)
    assert len(poss1.greenletters) == 1
    assert poss1.greenletters[0] == "l"
    assert poss1.greenindices[0] == 1
    assert len(poss1.blackletters) == 4
    assert poss1.blackletters[1] == "a"
    assert poss1.blackindices[1] == 2

def test_update_list():
    # test for easy green and black cases
    poss1 = PossibleWords.PossibleWords(("grate", "bonus", "raise", "amass", "cover", "phase"))
    guess1 = WordGuess.WordGuess("broke", "bbbbg")
    poss1.update_letters(guess1)
    poss1.update_list(guess1)
    assert len(poss1.possible) == 2

