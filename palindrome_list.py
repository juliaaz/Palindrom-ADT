"""
Palindrome class realization.
"""

from linkedstack import LinkedStack

class Palindrome:
    """
    Class for Palindrome representation.
    """
    def __init__(self):
        """
        Constructor for Palindrome.
        """
        self.english = self.find_palindromes('words.txt', 'palindrome_en.txt')
        self.ukrainian = self.find_palindromes('base.lst', 'palindrome_uk.txt')
        self.write_to_file('palindrome_en.txt', self.english)
        self.write_to_file('palindrome_uk.txt', self.ukrainian)

    @staticmethod
    def read_file(filename):
        """
        Method reads file and converts data to list.
        """
        output = []
        with open(filename, 'r', encoding='utf-8') as file:
            for word in file:
                output.append(word.split()[0].strip())

        return output

    @staticmethod
    def write_to_file(filename, words):
        """
        Method writes data to file.
        """
        with open(filename, 'w') as file:
            for word in words:
                file.write(word + '\n')
                # print(word, file=file)

    def find_palindromes(self, from_file, in_file):
        """
        Method for finding palindromes and writing them to file.
        """
        output = []
        filee = self.read_file(from_file)
        for word in filee:
            if self.check_word(word):
                output.append(word)
        self.write_to_file(in_file, output)
        return output

    @staticmethod
    def check_word(word):
        """
        Method for checking the word if it's palindrome.
        """
        stack = LinkedStack()
        for letter in word[:len(word) // 2]:
            stack.push(letter)
        for letter in word[len(word) % 2 + len(word) // 2:]:
            item = stack.pop()
            if letter != item:
                return False
        return True
