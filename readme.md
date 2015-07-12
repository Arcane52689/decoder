# Decoder App
An app built in python to use common decryption methods on an encrypted text.  Uses tkinter to form a user interface.  Uses a word tree to keep track of the dictionary, as well as generate possible words.

##Ciphers
###Ceasar Cipher
A simple function that prints out all 26 possible combinations of a caesar cipher.  Future improvements will include an option to eliminate options where most of the words aren't in the dictionary(probably ~75%).


### Substitution Cipher
This code is broken into two pieces. An aid for a human solver, and a computer solver.

#### Human Solver
This is simply a UI that show the letter frequencies and allows the user to make guess underneath the letter.  When they click update, the message changes and the user can proceed until it's solved.

#### Computer Solver
This code is a bit more complex.  It uses 2 classes, a Words and Solvers.  
##### Word
The Word class acts as a miniature solver for each word in the message. It uses a word tree to generate all possible solutions of a word.  It can then find all the indices of an encrypted letter, and search for common solutions for that letter, as well as keep track of the number of occurrences.
##### Solver
The Solver class acts as a head for the collection of Word classes. The Solver will first create a hash of all the possible solutions for each letter.  It will then find all letters with one solution, and apply those.  It will continue this process until it there are no letters with a single solution.  It will then proceed to guess based on the letter with lowest number of solutions and the best ratios. ie, it will pick a pair before a triplet, and a pair with counts 9 and 2 before it picks a pair with counts 10 and 10.  It will then recursively generate all the possible solutions of the message- all possible being any time it has to make a guess, it will give the solutions for all options of that guess.
