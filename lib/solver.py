class Solver(object):

    def __init__(self, encrypted, decrypted, known, word_tree):
        self.encrypted_words = encrypted.split()
        self.decrypted_words = decrypted.split()
        self.word_tree = []





class Word(object):

    def __init__(self, str, word_tree):
        self.word_tree = word_tree
        self.encrypted = encrypted
        self.decrypted = decrypted
        self.find_possible_words()
        self.solved = False

    def find_possible_words(self):
        self.possible_words = self.word_tree.all_words(self.decrypted)
        self.set_frequencies()

    
    def number_of_possibilities(self):
        return len(self.possible_words)


    def all_words(self):
        return self.possible_words

    def set_frequencies(self):
        self.frequencies = {}
        for i in range(0, len(self.encryped)):
            if self.decrypted[i] == "_":
                self.frequencies[self.encryped[i]] = self.letters_at_index(i)

    def get_frequencies(self):
        return self.frequencies()

    def letters_at_index(self, index):
        result = {}
        for word in self.possible_words:
            result[word[index]] = result.get(word[index], 0) + 1
        return result
