"""Word Finder: finds random words from a dictionary."""
import random


class WordFinder:
    ...
    def __init__(self, file):
        self.file = open(file)
        self.words = self.read_file()

    def read_file(self):
        words_list = self.file.readlines()
        words = [word.strip() for word in words_list]
        return words
        f.close()

    def random(self):
        return random.choice(self.words)

class RandomWordFinder(WordFinder):
      def read_file(self):
        words_list = self.file.readlines()
        words = [word.strip() for word in words_list if not word.startswith("#")]
        return words
        f.close()

     

