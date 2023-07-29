import random

class Datastore():
    
    def __init__(self):
        with open("dictionary.txt") as wordfile:
            self.Allword = wordfile.read().splitlines()
        #print(self.Allword)
        with open("hints.txt") as hintfile:
            self.wordhints = hintfile.read().splitlines()
        #print(self.wordhints)

    def get_word(self):
        # to return the word from the text file
        self.word1 = ""
        while len(self.word1) < 3:
            self.word1 = random.choice(self.Allword)
        
        return self.word1 
    
    def get_index(self):
        index = self.Allword.index(self.word1)
        return self.wordhints[index]