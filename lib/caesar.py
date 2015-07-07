
from Tkinter import *

class Caesar(object):
    def __init__(self, message):
        self.message = message.lower()


    def decrypt(self, shift):
        result = ""
        for i in range(0, len(self.message)):
            if self.message[i] == " ":
                result += " "
            else:
                new_letter_ord = ((ord(self.message[i]) - 97 + shift) % 26) + 97
                result += chr(new_letter_ord)
        return result

    def all_results(self):
        result = []
        for i in range(0, 26):
            result.append(self.decrypt(i))

        return result



    def display(self, master):
        self.frame = Frame(master)
        self.frame.grid()
        results = self.all_results()

        for i in range(0,26):
            label = Label(self.frame, text = results[i])
            label.grid(row = i, column = 0)


        close_button = Button(self.frame, text = "close", command = self.close)
        close_button.grid(row = 26, column = 0)


    def close(self):
        self.frame.destroy()
