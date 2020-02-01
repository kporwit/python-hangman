from functions import word_check, print_hangman
 
def check_guessed_letter(guessed_letter, word):
    print "letter", guessed_letter, "word", word
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
template_list = [0] * letters_count
while(tries != 13):
    index = check_guessed_letter(guessed_letter, word)
    if(index == False):
        print "Wrong guess"
        print template
        print_hangman(tries)
        tries += 1
    else:
        print "Nice!"
        template = ""
        for iter in xrange(0, letters_count):
            if(index[iter] != 0):
                template_list[iter] = index[iter]
        for iter in xrange(0, letters_count):
           if(template_list[iter] != 0):
               template += template_list[iter]
           else:
               template += '_'
        print template


    guessed_letter = raw_input("Guess the letter: ")

