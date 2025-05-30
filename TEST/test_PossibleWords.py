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
    # singleletter list case
    guess4 = WordGuess.WordGuess("boost", "bybbb")
    poss1.update_letters(guess4)
    assert len(poss1.singleletters) == 1
    assert len(poss1.yellowletters) == 4
    assert poss1.singleletters[0] == "o"
    guess5 = WordGuess.WordGuess("sweep", "bbgbb")
    poss1.update_letters(guess5)
    assert len(poss1.singleletters) == 2
    assert len(poss1.yellowletters) == 5
    assert poss1.singleletters[1] == "e"
    
    # double letter and triple letter test cases
    poss2 = PossibleWords.PossibleWords(("flock", "donut", "shale"))
    guess6 = WordGuess.WordGuess("moron", "bybyb")
    poss2.update_letters(guess6)
    assert len(poss2.doubleletters) == 1
    guess7 = WordGuess.WordGuess("beret", "bgbyb")
    poss2.update_letters(guess7)
    assert len(poss2.doubleletters) == 2

    guess8 = WordGuess.WordGuess("ababa", "gbgby")
    poss2.update_letters(guess8)
    assert len(poss2.tripleletters) == 1




def test_update_list():
    # test for easy green and black cases
    poss1 = PossibleWords.PossibleWords(("grate", "bonus", "raise", "amass", "cover", "phase"))
    guess1 = WordGuess.WordGuess("broke", "bbbbg")
    poss1.update_letters(guess1)
    poss1.update_list()
    assert len(poss1.possible) == 1

    # test for yellow case
    poss2 = PossibleWords.PossibleWords(("grate", "bonus", "raise", "amass", "cover", "phase"))
    guess2 = WordGuess.WordGuess("broke", "bybbg")
    poss2.update_letters(guess2)
    poss2.update_list()
    assert len(poss2.possible) == 1


    # test for case of duplicate yellows
    poss3 = PossibleWords.PossibleWords(("coral", "motor", "taboo"))
    guess3 = WordGuess.WordGuess("goose", "byybb")
    poss3.update_letters(guess3)
    poss3.update_list()
    assert len(poss3.possible) == 1

    # test for black + yellow case
    poss4 = PossibleWords.PossibleWords(("coral", "motor", "tabbo"))
    guess4 = WordGuess.WordGuess("oxxxo", "ybbbb")
    poss4.update_letters(guess4)
    poss4.update_list()
    assert len(poss4.possible) == 1

    # multiple guesses
    poss5 = PossibleWords.PossibleWords(("abcde", "abxyz", "xxbyd", "bcxza", "dabcz", "yaaaa"))
    guess5 = WordGuess.WordGuess("agggg", "ybbbb")
    poss5.update_letters(guess5)
    poss5.update_list()
    assert len(poss5.possible) == 3

    guess6 = WordGuess.WordGuess("gaggg", "bgbbb")
    poss5.update_letters(guess6)
    poss5.update_list()
    assert len(poss5.possible) == 2

    guess7 = WordGuess.WordGuess("aaggg", "ygbbb")
    poss5.update_letters(guess7)
    poss5.update_list()
    assert len(poss5.possible) == 1
    



    

