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
            words = [line.strip() for line in file]
            for word in words:
                print(f"Read word: {word}")
            return words

    def random(self):
        """Return a random word from the list of words."""
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """Finds random words from a dictionary, excluding blank lines and comments."""
    
    def read_words(self, path):
        """Read words from a file, excluding blank lines and comments."""
        with open(path, 'r') as file:
            return [line.strip() for line in file if line.strip() and not line.startswith('#')]


wf = WordFinder(r"C:\Users\lobel\OneDrive\Documents\SpringBoard\Python\Section 3 OOP\words2.txt")
print(wf.random())