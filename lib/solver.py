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





    def combine_results(self, dict1, dict2):
        result = {}
        for key in dict1.getkeys():
            if dict2.get(key, False):
                result[key] = dict1[key] + dict2[key]
        return result




class Word(object):

    def __init__(self, encrypted, decrypted, word_tree, known):
        self.word_tree = word_tree
        self.encrypted = encrypted
        self.decrypted = decrypted
        self.find_possible_words()
        self.solved = False
        self.known = known

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
        return self.frequencies

    def letters_at_index(self, index):
        result = {}
        for word in self.possible_words:
            result[word[index]] = result.get(word[index], 0) + 1
        return result

    def indices_of_letter(self, letter):
        result = []
        for i in range(0, len(self.encrypted)):
            if letter == self.encrypted[i]:
                result.append(i)
        return result


    def possible_solutions(self, letter):
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
        result = {}
        for key in dict1.getkeys():
            if dict2.get(key, False):
                result[key] = dict1[key] + dict2[key]
        return result
