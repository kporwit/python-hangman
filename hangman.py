def word_check(given_word):
    given_word = given_word.lower()
    for letter in given_word:
        if(letter.isalpha() == False):
            print "Word must conatin only letters"
            return 1


word = raw_input("Define word for guessing: ")
word_check(word)
