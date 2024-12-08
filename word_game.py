import random
class WordGame:
    def __init__(self, word_list):
        #a list of words and selects a random word.
        self.word_list = word_list
        self.current_word = random.choice(self.word_list)
        self.attempts = 0

def guess_word(self, guess):
    #check if the guessed word maches the current world.
    if re.fullmatch(r'[a-zA-Z]+', guess):
        self.attempts += 1
        return guess.lower() == self.current_word.lower()
    else:
        return False
    
class ExtendedWordGame(WordGame):
    def provide_hint(self):
    #Gives the first letter as a hint
        return f"Hint: The word starts with '{self.current_word[0]}'."
    