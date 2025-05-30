# change to SRC.WordGuess as WordGuess to allow for unit testing
import WordGuess as WordGuess
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

        # list keeps track of single/double/triple letters
        self.singleletters = []
        self.doubleletters = []
        self.tripleletters = []


    # updates letters for the variables of the object
    def update_letters(self, guess: WordGuess):

        currentyellows = []
        currentgreens = []

        # updates new green letters
        for i in range(5):
            if guess.colorS[i] == "g":
                currentgreens.append(guess.wordS[i])
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
        
        
        

        # updates new yellow letters
        for i in range(5):
            if guess.colorS[i] == "y":
                currentyellows.append(guess.wordS[i])
                # if the letter in the guess is already a yellow letter in the list
                if guess.wordS[i] in self.yellowletters:
                    dup = False
                    # if the yellow letter in the guess has the same index as a yellow letter already in the list
                    for j in range(len(self.yellowletters)):
                        if self.yellowletters[j] == guess.wordS[i]:
                            if self.yellowindices[j] == i:
                                dup = True
                    if dup == False:
                        self.yellowletters.append(guess.wordS[i])
                        self.yellowindices.append(i)
                else:
                    self.yellowletters.append(guess.wordS[i])
                    self.yellowindices.append(i)
        
        # updates doubleletter and tripleletter lists
        for i in range(5):
            if currentgreens.count(guess.wordS[i]) == 2:
                if currentyellows.count(guess.wordS[i]) == 1:
                    if not guess.wordS[i] in self.tripleletters:
                        self.tripleletters.append(guess.wordS[i])
                if currentyellows.count(guess.wordS[i]) == 0:
                    if not guess.wordS[i] in self.doubleletters:
                        self.doubleletters.append(guess.wordS[i])
            if currentgreens.count(guess.wordS[i]) == 1:
                if currentyellows.count(guess.wordS[i]) == 2:
                    if not guess.wordS[i] in self.tripleletters:
                        self.tripleletters.append(guess.wordS[i])
                if currentyellows.count(guess.wordS[i]) == 1:
                    if not guess.wordS[i] in self.doubleletters:
                        self.doubleletters.append(guess.wordS[i])
            if currentgreens.count(guess.wordS[i]) == 0:
                if currentyellows.count(guess.wordS[i]) == 2:
                    if not guess.wordS[i] in self.doubleletters:
                        self.doubleletters.append(guess.wordS[i])

        # updates new black letters
        for i in range(5):
            if guess.colorS[i] == "b":
                # for special case where there are duplicate letters in guess where one is yellow and others are black
                # a duplicate letter that is black after a yellow should be treated as a yellow at the certain index
                # a duplicate letter that is black after a green should be treated as a yellow at the certain index
                if guess.wordS[i] in currentyellows:
                    self.yellowletters.append(guess.wordS[i])
                    self.yellowindices.append(i)
                    if not guess.wordS[i] in self.singleletters:
                        self.singleletters.append(guess.wordS[i])
                elif guess.wordS[i] in self.greenletters:
                    self.yellowletters.append(guess.wordS[i])
                    self.yellowindices.append(i)
                    if not guess.wordS[i] in self.singleletters:
                        self.singleletters.append(guess.wordS[i])
                else:
                    if not guess.wordS[i] in self.blackletters:
                        self.blackletters.append(guess.wordS[i])
    


    # updates the list of possible words in the wordle dictionary
    def update_list(self):

        removeset = set()

        # removes all words from possible list that are not aligned with the green letters
        for i in range(len(self.greenletters)):
            for pos in self.possible:
                if not self.greenletters[i] == pos[self.greenindices[i]]:
                    removeset.add(pos)

        

        # removes all words from possible list that include any black letters        
        for i in range(len(self.blackletters)):
            for pos in self.possible:
                if self.blackletters[i] in pos:
                    removeset.add(pos)

        # removes all words from possible list that have a letter in its yellow square
        for i in range(len(self.yellowletters)):
            for pos in self.possible:
                if self.yellowletters[i] == pos[self.yellowindices[i]]:
                    removeset.add(pos)
        
        # removes all words from possible list that do no have a letter that is yellow
        for i in range(len(self.yellowletters)):
            for pos in self.possible:
                if not self.yellowletters[i] in pos:
                    removeset.add(pos)


        # removes all words that do not have the necessary amount of letters in the doubleletter or tripleletter lists
        
        for i in range(len(self.doubleletters)):
            for pos in self.possible:
                if not pos.count(self.doubleletters[i]) >= 2:
                    removeset.add(pos)

        for i in range(len(self.tripleletters)):
            for pos in self.possible:
                if not pos.count(self.tripleletters[i]) >= 3:
                    removeset.add(pos)
        
        # removes all words that have more than one of letters in the list singleletters

        for i in range(len(self.singleletters)):
            for pos in self.possible:
                if pos.count(self.singleletters[i]) > 1:
                    removeset.add(pos)
        
        
        
        # removes all elements from self.possible that are in the set
        for removal in removeset:
            if removal in self.possible:
                self.possible.remove(removal)
        
        

                








                    





        
        

        

         

    