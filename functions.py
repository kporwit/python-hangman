def word_check(given_word):
    if( not given_word):
        print "Word must conatin only letters. Try again."
        return 1
    elif( len(given_word) < 4):
        print "Please try harder! At least four signs."
        return 1
    elif( len(given_word) > 40):
        print "Hold on cowboy, that is a really long world! 40 signs maximum."
        return 1
    given_word = given_word.lower()
    for letter in given_word:
        if(letter.isalpha() == False):
            print "Word must conatin only letters. Try again."
            return 1
    return given_word

def check_guessed_letter(guessed_letter, word):
    if( not guessed_letter):
        print "This counts as wrong answer. Insert letter next time."
        return False
    elif( len(guessed_letter) > 1):
        print "This counts as wrong answer. Insert ONE letter next time."
        return False
    elif( guessed_letter.isalpha() == False):
        print "This counts as wrong answer. Insert ONLY alphabet character next time."
        return False
    index = []
    for letter in word:
        if(letter == guessed_letter):
            index.append(guessed_letter)
        else:
            index.append(0)
    if( word.find(guessed_letter) >= 0):
        return index
    else:
        return False

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
