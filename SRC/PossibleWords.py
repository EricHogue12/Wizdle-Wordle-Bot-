import SRC.WordGuess as WordGuess
# defines the list of possible words left from the wordle dictionary given the results of all the previous guesses
class PossibleWords:
    
    # constructor intended for construction at the beginning of the main class before guesses are made
    # ideally only one object is ever created
    def __init__(self, words: tuple):
        # converts the tuple into a list
        self.possible = list(words)
        self.greenletters = []
        self.blackletters = []
        # list of index (0,1,2,3,4) where green/black occurs *** the first element of greenletters maps to the first 
        # element of greenindices and so on
        self.greenindices = []
        self.blackindices = []

    # updates letters for the variables of the object
    def update_letters(self, guess: WordGuess):
        # updates green letters
        for i in range(5):
            if guess.colorS[i] == "g":
                self.greenletters.append(guess.wordS[i])
                self.greenindices.append(i)

        # updates black letters for when there are no yellows
        if not "y" in guess.colorS:
            for i in range(5):
                if guess.colorS[i] == "b":
                    self.blackletters.append(guess.wordS[i])
                    self.blackindices.append(i)

    # updates the list of possible words in the wordle dictionary
    def update_list(self, guess: WordGuess):
        
        # removes all words from possible list that are not aligned with the green letters
        for i in range(len(self.greenletters)):
            for pos in self.possible:
                print(pos)
                if not self.greenletters[i] == pos[self.greenindices[i]]:
                    self.possible.remove(pos)

        
        # removes all words from possible list that include any black letters        
        for i in range(len(self.blackletters)):
            for pos in self.possible:
                if self.blackletters[i] in pos:
                    self.possible.remove(pos)

         

    