import WordGuess
# defines the list of possible words left from the wordle dictionary given the results of all the previous guesses
class PossibleWords:
    
    # constructor intended for construction at the beginning of the main class before guesses are made
    def __init__(self, words: tuple):
        # converts the tuple into a list
        self.possible = list(words)
        self.blackletters = []
        self.greenletters = []
        # list of index (0,1,2,3,4) where green occurs *** the first element of greenletters maps to the first element of greenindices
        # and so on
        self.greenindices = []

    # updates green letters and black letters for the variables of the object
    def update_letters(self, guess: WordGuess):
        for i in range(5):
            if guess.colorS[i] == "b" or guess.colorS[i] == "B":
                self.blackletters.append(guess.wordS[i])
            if guess.colorS[i] == "g" or guess.colorS[i] == "G":
                self.greenletters.append(guess.wordS[i])
                self.greenindices.append(i)

    # updates the list of possible words in the wordle dictionary (includes processing of yellow letters)
    def update_list(self, guess: WordGuess):
        # removes all words from possible list that include any black letters        
        for i in range(len(self.blackletters)):
            for j in range(len(self.possible)):
                if self.blackletters[i] in self.possible[j]:
                    self.possible.remove(self.possible[j])
        # removes all words from possible list that 

    