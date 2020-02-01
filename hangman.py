from functions import word_check, print_hangman
 
def check_guessed_letter(guessed_letter, word):
    print "letter", guessed_letter, "word", word
    for letter in word:
        if(guessed_letter == letter):
            index = word.index(guessed_letter)
            return index
    return False

print "WELCOME TO THE HANGMAN GAME"
print_hangman(12) #at 12 the full hangman picture is printed
word_check_return = 1

while word_check_return != 0:
    word = raw_input("Define word for guessing: ")
    word_check_return = word_check(word)

letters_count = len(word)
template = "_"*letters_count
print "Let's start the game..."
print template
guessed_letter = raw_input("Guess the letter: ")
tries = 1
while(tries != 13):
    index = check_guessed_letter(guessed_letter, word)
    if(index == False):
        print "Wrong guess"
        print template
        print_hangman(tries)
        tries += 1
    else:
        print "Nice!"
        first = template[:index]
        second = template[(index+1):]
        template = first + guessed_letter + second
        print template
    guessed_letter = raw_input("Guess the letter: ")

