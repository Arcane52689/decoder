class WordTree(object):

    def __init__(self, file_name):
        self.head = LetterNode("")
        self.build(file_name)


    def build(self, file_name):
        file = open()
        while True:
            line = file.readline
            if line == None:
                break

            word = line.strip()
            self.head.add_word(word)

    def check_word(self, word):
        return self.head.check_word(word)


class LetterNode(object):
    def __init__(self, letter):
        self.is_word = False
        self.letter = letter
        self.children = {}

    def add_word(self, word):
        if len(word) == 0:
            self.set_word()
        else
            next_letter = self.find_or_create(letter)
            next_letter.add_word(word[1:len(word)])


    def addChild(self, letter):
        child = LetterNode(letter)
        self.children[letter] = child
        return child


    def getChildren(self):
        return self.children

    def find_or_create(self, letter):
        if self.children.get(letter,False):
            return self.children[letter]
        else:
            return self.addChild(letter)

    def get_child(self, letter):
        return self.children.get(letter, None)


    def set_word(self):
        self.is_word = True

    def check_word(self, word):
        if len(word) == 0:
            return self.is_word
        else:
            child = self.get_child(word[0])
            if child:
                return child.check_word(word[1:len(word)])
            else:
                return False
