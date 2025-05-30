# change to SRC.ValidWords as Validwords to allow for unit testing
import ValidWords as ValidWords

# class which deals with the guesses that the user enters in that they made and which letters are yellow, green, or grey
class WordGuess:

    # constructor that creates the word guess object and error checks the parameters
    def __init__(self, wordString, colorString):
        if not isinstance(wordString, str):
            raise TypeError("user word guess should be a String")
        if not isinstance(colorString, str):
            raise TypeError("user color input should be a String")
        if not len(wordString) == 5:
            raise ValueError("user word guess should be 5 letters long")
        if not len(colorString) == 5:
            raise ValueError("user color input should be 5 letters long")
        for letter in wordString:
            if not letter.isalpha():
                raise ValueError("user word guess should be only letters")
        
        for letter in colorString:
            if not letter.isalpha():
                raise ValueError("user color input should be only letters")
            if not (letter == "y" or letter == "g" or letter == "b"):
                raise ValueError("user color input should only contain the letters G -> green, Y -> yellow, or B -> black")
             
        self.wordS = wordString
        self.colorS = colorString
    
    # checks if the guess the user made was a valid five letter word
    def valid_word(self):
        validWords = ValidWords.ValidWords().validWS
        word1 = self.wordS
        if not word1 in validWords:
            raise ValueError("user word guess should be a real word")
        
    

     