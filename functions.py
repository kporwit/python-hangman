def word_check(given_word):
    given_word = given_word.lower()
    for letter in given_word:
        if(letter.isalpha() == False):
            print "Word must conatin only letters. Try again."
            return 1
    return 0


def print_hangman(wrong_guesses):
    if( wrong_guesses == 1 ):
        print """








-------------------------------
"""
    if( wrong_guesses == 2 ):
        print """







       / \\
-------------------------------
"""
    if( wrong_guesses == 3 ):
        print """
         
        |
        |
        |
        |
        |
        |
       / \\
-------------------------------
"""
    if( wrong_guesses == 4 ):
        print """
         ____
        |
        |
        |
        |
        |
        |
       / \\
-------------------------------
"""
    if( wrong_guesses == 5 ):
        print """
         ____
        |    |
        |
        |
        |
        |
        |
       / \\
-------------------------------
"""
    if( wrong_guesses == 6 ):
        print """
         ____
        |    |
        |    O
        |
        |
        |
        |
       / \\
-------------------------------
"""
    if( wrong_guesses == 7 ):
        print """
         ____
        |    |
        |    O
        |    |
        |
        |
        |
       / \\
-------------------------------
"""
    if( wrong_guesses == 8 ):
        print """
         ____
        |    |
        |    O
        |   /|
        |
        |
        |
       / \\
-------------------------------
"""
    if( wrong_guesses == 9 ):
        print """
         ____
        |    |
        |    O
        |   /|\\
        |
        |
        |
       / \\
-------------------------------
"""
    if( wrong_guesses == 10 ):
        print """
         ____
        |    |
        |    O
        |   /|\\
        |    |
        |
        |
       / \\
-------------------------------
"""
    if( wrong_guesses == 11 ):
        print """
         ____
        |    |
        |    O
        |   /|\\
        |    |
        |   /
        |
       / \\
-------------------------------
"""
    if( wrong_guesses == 12 ):
        print """
         ____
        |    |
        |    O
        |   /|\\
        |    |
        |   / \\
        |
       / \\
-------------------------------
"""
