class Solver(object):

    def __init__(self, encrypted, decrypted, known, word_tree):
        self.word_tree = word_tree
        self.known = known
        self.words = []
        self.build_words(encrypted, decrypted)

    def build_words(self, encrypted, decrypted):
        encrypted_list = encrypted.split()
        decrypted_list = decrypted.split()
        for i in range(0, len(encrypted_list)):
            word = Word(encrypted, decrypted, self.word_tree, self.known)
            self.words.append(word)

    def check_all_words(letter):
        result = self.words[0].possible_solutions(letter)
        for i in range(1, len(self.words)):
            result2 = self.words[i].possible_solutions(letter)
            result = self.combine_results(result, result2)
        return result

    def create_possibilities(self):
        self.possibilities = {}
        for i in range(0, 26):
            letter = chr(97 + i)
            if letter not in self.known.getkeys():
                self.possibilities[letter] = self.check_all_words(letter)
        return self.possibilities

    def check_for_solutions(self):
        keys = self.possiblities.getkeys()
        for key in keys:
            if len(self.possibilities[key]) == 0:
                return False
            if len(self.possibilities[key]) == 1:
                self.update_known(key, self.possibilites[key][0])
        return True

    def combine_results(self, dict1, dict2):
        result = {}
        for key in dict1.getkeys():
            if dict2.get(key, False):
                result[key] = dict1[key] + dict2[key]
        return result

    def update_known(self, encrypted_letter, decrypted_letter):
        self.known[encrypted_letter] = decrypted_letter
        for word in self.words:
            word.update_decrypted(encrypted_letter, decrypted_letter)




class Word(object):
    # A class to represent the words in an encrypted message.  Each word keeps track of it's encrypted and decrypted states, using '_' for unknown characters
    def __init__(self, encrypted, decrypted, word_tree, known):
        self.word_tree = word_tree
        self.encrypted = encrypted
        self.decrypted = decrypted
        self.find_possible_words()
        self.solved = False
        self.known = known

    def find_possible_words(self):
        """Finds all possible words in the english dictionary"""
        self.possible_words = self.word_tree.all_words(self.decrypted)
        self.set_frequencies()


    def number_of_possibilities(self):
        """Returns the number of possible words"""
        return len(self.possible_words)


    def all_words(self):
        """Returns self.possible_words"""
        return self.possible_words

    def set_frequencies(self):
        """Determines the frequency of letter occurences in possible words at different indices"""
        self.frequencies = {}
        for i in range(0, len(self.encryped)):
            if self.decrypted[i] == "_":
                self.frequencies[self.encryped[i]] = self.letters_at_index(i)

    def get_frequencies(self):
        return self.frequencies

    def letters_at_index(self, index):
        """ Returns all the possible letters and their counts at a certain index"""
        result = {}
        for word in self.possible_words:
            result[word[index]] = result.get(word[index], 0) + 1
        return result

    def indices_of_letter(self, letter):
        """Finds all the indices of an encrypted letter in a word"""
        result = []
        for i in range(0, len(self.encrypted)):
            if letter == self.encrypted[i]:
                result.append(i)
        return result


    def possible_solutions(self, letter):
        """Finds all the possible solutions of a letter at a given word"""
        indices = self.indices_of_letter(letter)
        if len(indices) == 0:
            return {}
        elif len(indices) == 1:
            return self.letters_at_index(indices[0])
        else:
            result = self.letters_at_index(indices[0])
            for i in range(1, len(indices)):
                result2 = self.letters_at_index(indices[i])
                result = combine_results(result, result2)
            return result


    def combine_results(self, dict1, dict2):
        """ A simple hash intersection function that combines the counts of letters  This way if a hash of { a: 1, b: 2, d: 1 } were combined with { a: 1, b: 3, c: 1 }, the result would be { a: 2, b: 5 }"""
        result = {}
        for key in dict1.getkeys():
            if dict2.get(key, False):
                result[key] = dict1[key] + dict2[key]
        return result

    def update_decrypted(self, encrypted, decrypted):
        """ Updates the encrypted word with a solution.  Then reruns find_possible_words."""
        indices = self.indices_of_letters(encrypted)
        decrypted_arr = self.decrypted.split("")
        for index in indices:
            decrypted_arr = decrypted
        self.decrypted = "".join(decrypted_arr)
        self.find_possible_words()
