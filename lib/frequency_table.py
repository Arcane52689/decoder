class FrequencyTable(object):
    def __init__(self, message):
        self.message = message
        self.count = {}
        self.build()

    def build(self):
        letter = "a"
        for i in range(0,len(self.message)):
            letter=self.message[i]
            self.count[letter]= self.count.get(letter, 0) + 1

    def count_of(self, letter):
        return self.count.get(letter, 0)
