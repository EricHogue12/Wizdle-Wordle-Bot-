import SRC.WordGuess as WordGuess
# defines the list of possible words left from the wordle dictionary given the results of all the previous guesses
class PossibleWords:
    
    # constructor intended for construction at the beginning of the main class before guesses are made
    # ideally only one object is ever created
    def __init__(self, words: tuple):
        # converts the tuple into a list
        self.possible = list(words)
        self.greenletters = []
        self.yellowletters = []
        self.blackletters = []
        # list of index (0,1,2,3,4) where green/yellow occurs *** the first element of greenletters maps to the first 
        # element of greenindices and so on
        self.greenindices = []
        self.yellowindices = []

    # updates letters for the variables of the object
    def update_letters(self, guess: WordGuess):
        # updates new green letters
        for i in range(5):
            if guess.colorS[i] == "g":
                # if the letter in the guess is already a green letter in the list
                if guess.wordS[i] in self.greenletters:
                    dup = False
                    # if the green letter in the guess has the same index as a green letter already in the list
                    for j in range(len(self.greenletters)):
                        if self.greenletters[j] == guess.wordS[i]:
                            if self.greenindices[j] == i:
                                dup = True
                    if dup == False:
                        self.greenletters.append(guess.wordS[i])
                        self.greenindices.append(i)
                else:
                    self.greenletters.append(guess.wordS[i])
                    self.greenindices.append(i)

        # updates yellow letters
        for i in range(5):
            if guess.colorS[i] == "y":
                self.yellowletters.append(guess.wordS[i])
                self.yellowindices.append(i)

        # special case for yellow letters when it should be added to yellow list but not black list
        # (duplicate letters in guess that are misplaced but only one in word)
            #TODO

        # updates new black letters
        for i in range(5):
            if guess.colorS[i] == "b":
                if not guess.wordS[i] in self.blackletters:
                    self.blackletters.append(guess.wordS[i])
    


    # updates the list of possible words in the wordle dictionary
    def update_list(self, guess: WordGuess):
        
        # removes all words from possible list that are not aligned with the green letters
        for i in range(len(self.greenletters)):
            for pos in self.possible:
                if not self.greenletters[i] == pos[self.greenindices[i]]:
                    self.possible.remove(pos)

        
        # removes all words from possible list that include any black letters        
        for i in range(len(self.blackletters)):
            for pos in self.possible:
                if self.blackletters[i] in pos:
                    self.possible.remove(pos)

        # removes all words from possible list that have a letter in its yellow square
        for i in range(len(self.yellowletters)):
            for pos in self.possible:
                if self.yellowletters[i] == pos[self.yellowindices[i]]:
                    self.possible.remove(pos)
        
        # removes all words from possible list that do no have a letter that is yellow
        for i in range(len(self.yellowletters)):
            for pos in self.possible:
                if not self.yellowletters[i] in pos:
                    self.possible.remove(pos)

        
        

        

         

    