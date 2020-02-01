from functions import word_check, print_hangman
print "WELCOME TO THE HANGMAN GAME"
print_hangman(12)
#print """
#    WELCOME TO THE HANGMAN GAME
#         ____
#        |    |
#        |    O
#        |   /|\\
#        |    |
#        |   / \\
#        |
#       / \\
#-------------------------------
#"""

word_check_return = 1
while word_check_return != 0:
    word = raw_input("Define word for guessing: ")
    word_check_return = word_check(word)

letters_count = len(word)
print "Let's start the game..."



