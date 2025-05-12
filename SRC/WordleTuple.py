# the class for making the tuple of wordle words
class WordleTuple:
    
    # method for creating the WordleTuple object
    def __init__(self, *words):
        for w in words:
            if not isinstance(w, str):
                raise TypeError("invalid list of words")
        self.data = tuple(words)
    
    # returns the index of the given word in the tuple
    def index_of(self, word):
        i = 0
        while i<len(self.data):
            if self.data[i] == word:
                return i
            i+=1
        return -1
    
    # returns the tuple itself
    def getter_method(self):
        return self.data
    
    # returns the word in the tuple given the index
    def get_item(self, index):
        return self.data[index]
    
    # returns the length of the tuple
    def length(self):
        return len(self.data)

    
