def word_check(given_word):
    given_word = given_word.lower()
    for letter in given_word:
        if letter.isspace():
            print "Given word cannot contain spaces"
            return 1
        if letter.isdigit():
            print "Given word cannot contain numeric characters"
            return 2


word = raw_input("Define word for guessing: ")

