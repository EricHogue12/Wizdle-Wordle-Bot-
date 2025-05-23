import pytest
import SRC.PossibleWords as PossibleWords
import SRC.WordGuess as WordGuess

def test_constructor():
    poss1 = PossibleWords.PossibleWords(("hello", "hi"))
    assert poss1.possible == ["hello", "hi"]
    assert len(poss1.greenletters) == 0
    assert len(poss1.greenindices) == 0
    assert len(poss1.blackletters) == 0

def test_update_letters():
    poss1 = PossibleWords.PossibleWords(("flock", "donut", "shale"))
    guess1 = WordGuess.WordGuess("slate", "bgbbb")
    poss1.update_letters(guess1)
    assert len(poss1.greenletters) == 1
    assert poss1.greenletters[0] == "l"
    assert poss1.greenindices[0] == 1
    assert len(poss1.blackletters) == 4
    assert poss1.blackletters[1] == "a"
    guess2 = WordGuess.WordGuess("forum", "bgyby")
    poss1.update_letters(guess2)
    assert len(poss1.greenletters) == 2
    assert poss1.greenletters[1] == "o"
    assert poss1.greenindices[0] == 1
    assert len(poss1.blackletters) == 6
    assert poss1.blackletters[4] == "f"
    assert len(poss1.yellowletters) == 2
    assert poss1.yellowletters[0] == "r"
    assert poss1.yellowindices[1] == 4
    # testing green letter duplicate case (same letter and index) and black letter duplicate case
    guess3 = WordGuess.WordGuess("bogus", "bgbbb")
    poss1.update_letters(guess3)
    assert len(poss1.greenletters) == 2
    assert len(poss1.blackletters) == 8
    # testing yellow letter duplicate case
    guess4 = WordGuess.WordGuess("serum", "bbyby")
    poss1.update_letters(guess4)
    assert len(poss1.yellowletters) == 2

    # testing duplicate letters where some are yellow and others are black
    poss2 = PossibleWords.PossibleWords(("flock", "donut", "shale"))
    guess5 = WordGuess.WordGuess("goose", "bybbb")
    poss2.update_letters(guess5)
    assert len(poss2.blackletters) == 3
    assert poss2.blackletters[1] == "s"
    assert len(poss2.yellowletters) == 2
    assert poss2.yellowletters[1] == "o"
    assert poss2.yellowindices[1] == 2


def test_update_list():
    # test for easy green and black cases
    poss1 = PossibleWords.PossibleWords(("grate", "bonus", "raise", "amass", "cover", "phase"))
    guess1 = WordGuess.WordGuess("broke", "bbbbg")
    poss1.update_letters(guess1)
    poss1.update_list(guess1)
    assert len(poss1.possible) == 2

    

