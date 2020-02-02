#!/usr/bin/env python
from functions import word_check, print_hangman, check_guessed_letter
import getpass
 
print "WELCOME TO THE HANGMAN GAME"
print_hangman(12) #at 12 the full hangman picture is printed
word = 1

while word == 1:
    word = getpass.getpass("Ask other person to define word for guessing\n(the\
 input is hiden): ")
    word = word_check(word)

letters_count = len(word)
template = "Word: "
template += "_"*letters_count
print "Let's start the game..."
print template
wrong_guesses, good_guesses = 1, 1
template_list = [0] * letters_count
written_letter_list = []
while(wrong_guesses != 12):
    guessed_letter = raw_input("Guess the letter: ")
    index = check_guessed_letter(guessed_letter, word)
    written_letter_list.append(guessed_letter)
    if(index == False):
        print "Wrong guess"
        print template
        wrong_guesses += 1
    else:
        print "Nice!"
        good_guesses += 1
        template = "Word: "
        for iter in xrange(0, letters_count):
            if(index[iter] != 0):
                template_list[iter] = index[iter]
        for iter in xrange(0, letters_count):
           if(template_list[iter] != 0):
               template += template_list[iter]
           else:
               template += '_'
        print template
    print_hangman(wrong_guesses)
    print 'Already written letters:', str(written_letter_list)[1:-1]
    if(template_list.count(0) == 0):
        break
if(wrong_guesses == 12):
    print "You lost!"
else:
    print "Congratulations. You win!"
