from Tkinter import *

class FrequencyTable(object):
    def __init__(self, message):
        self.message = message
        self.count = {}
        self.build()

    def build(self):
        letter = "a"
        for i in range(0,len(self.message)):
            letter=self.message[i]
            if not self.count.get(letter, False):
                self.count[letter] = []
            self.count[letter].append(i)

    def count_of(self, letter):
        return len(self.count.get(letter, []))

    def indices_of(self, letter):
        return self.count.get(letter, [])


class DecryptTable(object):

    def __init__(self, master, message):
        self.message = message.lower()
        self.table = FrequencyTable(message)
        self.frame = Frame(master)
        self.labels = []
        self.entries = []

        self.build()

    def build_decrypted(self):
        self.decrypted = []
        for i in range(0, len(self.message)):
            if ord(self.message[i]) > 96 and ord(self.message[i])  < 123:
                self.decrypted.append("_")
            else:
                self.decrypted.append(self.message[i])

        self.decrypted_var = StringVar()
        self.decrypted_var.set("".join(self.decrypted))
        label = Label(self.frame, textvariable = self.decrypted_var)
        label.grid(row=0,column =0, columnspan =13, rowspan=2)


    def build(self):
        self.build_decrypted()
        self.frame.grid()
        self.build_letters()
        self.build_counts()
        self.build_entries()

        button = Button(self.frame, text= "update", command = self.update_letters)
        button.grid(row=8, column =4)


    def build_letters(self):
        for i in range(0, 26):
            label = Label(self.frame, text = chr(97 + i))
            hght = 2 if i < 13 else 5
            label.grid(row= hght , column = i % 13)
            self.labels.append(label)

    def build_counts(self):
        for i in range(0,26):
            label = Label(self.frame, text= self.table.count_of(chr(97 + i)))
            hght = 3 if i < 13 else 6
            label.grid(row = hght, column = i % 13)


    def build_entries(self):
        for i in range(0, 26):
            entry = Entry(self.frame, width = 5)
            hght = 4 if i < 13 else 7
            entry.grid(row = hght, column = i % 13)
            self.entries.append(entry)


    def update_letters(self):
        self.new_letters = []
        for i in range(0, 26):
            self.new_letters.append(self.entries[i].get())

        for i in range(0, 26):
            self.new_letters[i]
            letter = chr(97 + i)
            for index in self.table.indices_of(letter):
                self.decrypted[index] = self.new_letters[i]  if self.new_letters[i] else "_"

        self.decrypted_var.set("".join(self.decrypted))
