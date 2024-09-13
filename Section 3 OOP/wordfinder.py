import random

class WordFinder:
    """Finds random words from a dictionary."""
    
    def __init__(self, path):
        """Read words from a file and print the number of words read."""
        self.words = self.read_words(path)
        print(f"{len(self.words)} words read")

    def read_words(self, path):
        """Read words from a file and return a list of words."""
        with open(path, 'r') as file:
            return [line.strip() for line in file]

    def random(self):
        """Return a random word from the list of words."""
        return random.choice(self.words)

wf = WordFinder(r"C:\Users\lobel\OneDrive\Documents\SpringBoard\Python\Section 3 OOP\words.txt")
print(wf.random())