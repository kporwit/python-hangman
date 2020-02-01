#!/usr/bin/env python
from functions import word_check, print_hangman
 
print "WELCOME TO THE HANGMAN GAME"
print_hangman(12) #at 12 the full hangman picture is printed
word_check_return = 1

while word_check_return != 0:
    word = raw_input("Define word for guessing: ")
    word_check_return = word_check(word)

letters_count = len(word)
template = "Word: "
template += "_"*letters_count
print "Let's start the game..."
print template
wrong_guesses, good_guesses = 1, 1
template_list = [0] * letters_count
while(wrong_guesses != 12):
    guessed_letter = raw_input("Guess the letter: ")
    index = check_guessed_letter(guessed_letter, word)
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
    if(template_list.count(0) == 0):
        break
if(wrong_guesses == 12):
    print "You lost!"
else:
    print "Congratulations. You win!"
