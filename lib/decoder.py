from Tkinter import *
from caesar import *
from frequency_table import *
class Decoder:

    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.grid()
        self.build()

        # self.decoderGrid = Tk()


    def build(self):
        self.encrypted_entry = Text(self.frame, height = 10, width = 100)
        self.encrypted_entry.grid(row = 0, column = 0, rowspan=2, columnspan = 5)



        self.build_buttons()


    def build_buttons(self):
        self.caesar_button = Button(self.frame, text="caesar", command= self.caesar)

        self.caesar_button.grid(row = 2, column = 0)

        self.frequency_button = Button(self.frame, text ="frequency table", command=self.frequencies)
        self.frequency_button.grid(row = 2, column = 1)

    def update_message(self):
        self.message = self.encrypted_entry.get("1.0",END)


    def caesar(self):
        self.update_message()
        caesar = Caesar(self.message)

        caesar.display(self.frame)


    def frequencies(self):
        self.update_message()
        frequencies = DecryptTable(self,frame, self.message)





root = Tk()
d = Decoder(root)


mainloop()
