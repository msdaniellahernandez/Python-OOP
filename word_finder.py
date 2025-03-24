"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """Class to find random words from a dictionary file.
    
    Reads a file and creates a list of words, then provides
    functionality to fetch a random word.

    >>> wf = WordFinder("/Users/student/words.txt")
    3 words read

    >>> wf.random() in ['cat', 'dog', 'porcupine']
    True

    >>> wf.random() in ['cat', 'dog', 'porcupine']
    True
    """

    def __init__(self, path):
        """Initialize WordFinder with a file path and load words."""
        self.path = path
        self.words = self._load_words()
        print(f"{len(self.words)} words read")

    def _load_words(self):
        """Read the file and return a list of words."""
        with open(self.path, 'r') as file:
            return [line.strip() for line in file if line.strip()]

    def random(self):
        """Return a random word from the loaded list."""
        return random.choice(self.words)
if __name__ == "__main__":
    wf = WordFinder("words.txt")
    print(wf.random())  # Test printing a random word
