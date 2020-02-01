def word_check(given_word):
    given_word = given_word.lower()
    for letter in given_word:
        if(letter.isalpha() == False):
            print "Word must conatin only letters. Try again."
            return 1
        else:
            return 0

word_check_return = 1
while word_check_return != 0:
    word = raw_input("Define word for guessing: ")
    word_check_return = word_check(word)
